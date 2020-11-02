#Abrir uma imagem colorida, transformar para tom de cinza e aplique a técnica Crescimento de Regiões (Region Growing). Para isto, pegue uma imagem qualquer real, com tanto que a mesma possua um objeto se destaque do fundo. Inicialize a semente com um clique neste objeto, conforme o Tópico 21 e encontre uma regra de adesão que seja capaz de segmentar este objeto. Aplique o Crescimento de Regiões de forma iterativa, em que o algoritmo irá estabilizar apenas quando a região parar de crescer.

import cv2
import numpy  as np

#declara logo a semente, uma vez que iremos usar dentro de todas as funções que iremos criar
s = (0,0) 

#vamos iniciar a função Crescimento de Regiões ele irá receber duas coisas fundamentais para o crescimento: a imagem que é nela que vai crescer a semente e a semente em si que será introduzida com valor vazio
def CR(imcolor, s=None):

    #pega a forma da matriz/imagem
    ls, cs = imcolor.shape[:2] #linhas e colunas recebem o shape de  imcolor (que é a variável que armazena nossa imagem no computador)

    #pega o ponto da semente 
    xc, yc = s #semente recebe as coordenas xc, yc

    #criar a matriz que irá conter a região segmentada. Matriz de zeros com a mesma forma e tipo de a. LOgicamente pra ter a mesma forma e tipo de a, a função tem que receber a(no nosso caso, imcolor)
    matrizzero = np.zeros_like(imcolor)

    #marcar o ponto, semente
    matrizzero[xc, yc] = 255

    #cria variáveis para começar o loop afim de fazer a região crescer

    cr = 0
    pp = 1

    #vamos iniciar a pesquisa de vizinhança
    while pp != cr:

        pp = cr
        cr = 0

        for l in range(ls):
            for c in range(cs):
                if matrizzero[l, c] == 255:
                    if 130 < imcolor[l-1, c-1] < 230:
                        matrizzero[l-1, c-1] = 255
                        cr+=1
                    if 130 < imcolor[l-1, c] < 230:
                        matrizzero[l-1, c] = 255
                        cr+=1
                    if 130 < imcolor[l-1, c+1] < 230:
                        matrizzero[l-1, c+1] = 255
                        cr+=1
                    if 130 < imcolor[l, c-1] < 230:
                        matrizzero[l, c-1] = 255
                        cr+=1
                    if 130 < imcolor[l, c+1] < 230:
                        matrizzero[l, c+1] = 255
                        cr+=1
                    if 130 < imcolor[l+1, c-1] < 230:
                        matrizzero[l+1, c-1] = 255
                        cr+=1
                    if 130 < imcolor[l+1, c] < 230:
                        matrizzero[l+1, c] = 255
                        cr+=1
                    if 130 < imcolor[l+1, c+1] < 230:
                        matrizzero[l+1, c+1] = 255
                        cr+=1
    return matrizzero

#o clique. Vamos verificar se demos um clique esquerdo com o mouse

def clique(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #se o evento que ocorreu foi este, vamos retornar a nossa semente como variável global.
        global s


        #agora atualiza o que a nossa semente deve receber, ou seja, quais coordenadas. Lembre-se de que deve ser a do clique, uma vez que o evento que ocorreu foi verdadeiro e é o que está dentro da função
        s = (x, y)

#vamos agora à parte das exibições na tela

if __name__ == '__main__':

    #armazena a imagem na variável imcolor
    imcolor = cv2.imread('23.jpg')

    #transoforma a imagem em tom de cinza
    imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

    #CRIAR A JANELINHA PARA EXIBIR A IMAGEM ORIGINAL E ESPERAR PELO CLIQUE (observe que não é aqui ainda que iremos mostrar a imagem segmentada!!! cria a janela, mostra a original e espera pelo clique)
    cv2.namedWindow('Original', 1)
    cv2.imshow('Original', imcinza)
    cv2.setMouseCallback('Original', clique)
    cv2.waitKey(0)

    #vamoos armazena a imagem segmentada em uma variável a fim de que possamos exibi-la. Lembre-se de que a CR sempre vai receber a imagem e a semente
    imseg = CR(imcinza, s)

    #exibição do resultado final
    cv2.imshow('final', imseg)
    cv2.waitKey(0)



