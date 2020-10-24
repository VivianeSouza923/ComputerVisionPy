#Abrir uma imagem colorida e aplique a técnica Crescimento de Regiões (Region Growing). Para isto, pegue uma imagem qualquer real, com tanto que a mesma possua um objeto se destaque do fundo. Inicialize a semente com um clique neste objeto, conforme o Tópico 21 e encontre uma regra de adesão que seja capaz de segmentar este objeto. Aplique o Crescimento de Regiões de forma iterativa, em que o algoritmo irá estabilizar apenas quando a região parar de crescer. Este tópico diferencia-se do Tópico 23 por ser necessário encontrar uma regra que utilize os canais R, G e B simultanemante.

import cv2
import numpy as np

#vamos definir a varivel da nossa semente antes de tudo, pois iremos utiliza-la em diferentes funções
s = (0,0)

#Função Crescimento de Regiões
def CR(imcolor, s=None):

    #pega a forma da matriz/image
    ls, cs = imcolor.shape[:2]

    #pega o ponto da semente (xc, yc)
    xc, yc = s

    #pegar a cor da matriz
    color = imcolor[xc, yc]

    #criar uma matriz de zeros com a mesma forma e tipo da imagem
    matrizzero = np.zeros_like(imcolor)

    #marca a semente na imagem
    matrizzero[xc, yc] = color

    #criando variáveis para o loop
    cr = 0
    pp =1

    while pp != cr:
        pp = cr
        cr = 0

        for l in range(ls):
            for c in range(cs):
                if np.array_equal(matrizzero[l, c], color): #se a duas matrizes tiverem a mesma 
                    if np.array_equal(imcolor[l-1, c-1], color): #se a duas matrizes tiverem a mesma forma e elementos
                        matrizzero[l-1, c-1] = color #a matrizzero vai receber a matriz color
                        cr+=1
                    if np.array_equal(imcolor[l-1, c], color):
                        matrizzero[l-1, c] = color
                        cr+=1
                    if np.array_equal(imcolor[l-1, c+1], color):
                        matrizzero[l-1, c+1] = color
                        cr+=1
                    if np.array_equal(imcolor[l, c-1], color):
                        matrizzero[l, c-1] = color
                        cr+=1
                    if np.array_equal(imcolor[l, c+1], color):
                        matrizzero[l, c+1] = color
                        cr+=1
                    if np.array_equal(imcolor[l+1, c-1], color):
                        matrizzero[l+1, c-1] = color
                        cr+=1
                    if np.array_equal([l+1, c], color):
                        matrizzero[l+1, c] = color
                        cr+=1
                    if np.array_equal([l+1, c+1], color):
                        matrizzero[l+1, c+1] = color
                        cr+=1


        cv2.imshow('segmentada', matrizzero)
        cv2.waitKey(0)

    return matrizzero

def clique(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global s


        s = (x,y)


if __name__ == '__main__':

    imcolor = cv2.imread('23.jpg')

    imcolor = cv2.resize(imcolor, (0,0), fx=0.4, fy=0.4)


    cv2.namedWindow('Original', 1)
    cv2.imshow('Original', imcolor)
    cv2.setMouseCallback('Original', clique)
    cv2.waitKey(0)

    imseg = CR(imcolor, s)


    cv2.imshow('final', imseg)
    cv2.waitKey(0)
