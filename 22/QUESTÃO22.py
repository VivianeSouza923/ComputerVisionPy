#Faça o mesmo que o tópico 21, calculando no final o centroide do objeto segmentado pelo método Crescimento de Regiões 2D, apresentando a região segmentada em azul e o centroide em verde.

import cv2
import numpy as np

s = (0,0)



#aplique a técninca Crescimento de REgiões(Region Growing)
def CR(imcinza, s=None): #definindo a função... ela vai receber a minha imagem e a chamada semente que vai estar vazia, zerada etc.



    #pega a forma da matriz/imagem pra gente poder utilizar no for
    ls, cs = imcinza.shape[:2]

    #pegar o ponto do nosso s, que é nossa semente. 
    xc, yc = s

    #finalmente eu vou criar a matriz que será analisada dentro do for
    matriz = np.zeros_like(imcinza)

    #próximo passo é marcar o ponto no circulo
    matriz[xc, yc] = 255

    #vou iniciar as variáveis de contagem e comparação que vão fazer parte do crescimento da semente no laço
    cr = 0 
    pp = 1

    #processo de crescimento da semente
    while pp != cr:

        pp = cr
        cr = 0
        for l in range(ls):
            for c in range(cs):
                if matriz[l, c] == 255:
                    if imcinza[l-1, c-1]< 127:
                        matriz[l-1, c-1] = 255
                        cr += 1
                    if imcinza[l-1, c]< 127:
                        matriz[l-1, c] = 255
                        cr += 1
                    if imcinza[l-1, c+1]< 127:
                        matriz[l-1, c+1] = 255
                        cr+=1
                    if imcinza[l, c-1]< 127:
                        matriz[l, c-1] = 255
                        cr+=1
                    if imcinza[l, c]< 127:
                        matriz[l, c] = 255
                        cr+=1
                    if imcinza[l, c+1]< 127:
                        matriz[l, c+1] = 255
                        cr+=1
                    if imcinza[l+1, c-1]< 127:
                        matriz[l+1, c-1] = 255
                        cr+=1
                    if imcinza[l+1, c]< 127:
                        matriz[l+1, c] = 255
                        cr+=1
                    if imcinza[l+1, c+1]< 127:
                        matriz[l+1, c+1] = 255
                        cr+=1

    return matriz


#o clique (quando eu clicar pra fechar a imagem original, irá aparecer a imagem segmentada)
def cl(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: #se o que ocorreu foi um clique do mouse, minha semente será retornada.
        global s


        s = (x, y)

#vamos calcular a centroide da imagem agora
def centroide(imcolor):

    #inicializando as variáveis
    xc, yc = 0, 0

    #pega a forma pq vamos ver como a imagem como matriz
    ls, cs = imcolor.shape[:2]
    cont = 0 #contador

    #bora percorrer os quadrados da imagem
    for l in range(ls):
        for c in range(cs):
            if imcolor[l, c] == 255:
                xc+=l
                yc+=c
                cont+=1

    #cálculo do ponto médio(centróide)
    xc = int(xc/cont)
    yc = int(yc/cont)

    #retorna o resultado para ser utilizado logo a seguir
    return xc, yc



if __name__ == '__main__':

    #abrir uma imagem colorida
    imcolor = cv2.imread('e.jpg')

    #transformar para tom de cinza
    imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('Original Image', 1)
    cv2.imshow('Original image', imcinza)
    cv2.setMouseCallback('Original image', cl)
    cv2.waitKey(0)

    imseg = CR(imcinza, s)

    xc, yc= centroide(imseg)

    ls, cs = imseg.shape[:2]
    nueva = np.zeros([ls, cs, 3], np.uint8)


    nueva[np.where(imseg == 255)] = (255, 0, 0)

    cv2.circle(nueva, (yc, xc), 5, (0,255,0), -1)

    cv2.imshow('final', nueva)
    cv2.waitKey(0)

