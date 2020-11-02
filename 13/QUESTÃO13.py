#Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows). Apliquem uma convolução fazendo uma varredura na matriz utilizando as máscaras do operador gradiente Sobel (procurem no google). Visualizem os resultados e salvem. Obs: busquem compreender os resultados do operador Sobel (parece com o de canny, apenas parece).

#OBS.: Vai na horizontal, desce a primeira linha e depois sobe a terceira linha. Gx = ([-1 0 1] linha 1 [-2 0 2] linha 2 [-1 0 1] linha 3) * A, oond A é a matriz/imagem inicial
#OBS.: vai na vertical. Primeiro percorre a terceira linha da esquerda para a direita e depois a primeira linha. Gy = ([1 2 1] linha 1 [0 0 0] linha 2 [-1 -2 -1] linha 3) * A

import cv2
import numpy as np 
import math

#abrir uma imagem colorida
imcolor = cv2.imread('aplique-borbolertas-coloridas-324x324.jpg')

#transformar em tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#visualizar imagem de entrada
cv2.imshow('visualizar imagem de entrada', imcinza)

#Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows). 

#pra isso prmeiro vamos pegar a forma da imagem
linhas, colunas = imcinza.shape[:2]

#depois criar a matriz de zero
criamatrizzero = np.zeros((linhas, colunas), np.uint8) 

#Apliquem uma convolução fazendo uma varredura na matriz utilizando as máscaras do operador gradiente Sobel (procurem no google).
for linha in range(1, linhas-1):
    for coluna in range(1, colunas-1):
        Gx = imcinza[linha-1, coluna-1] * (-1) + imcinza[linha, coluna-1] * (-2) + \
             imcinza[linha+1, coluna-1] * (-1) + imcinza[linha-1, coluna+1] + \
             imcinza[linha, coluna+1] * 2 + imcinza[linha+1, coluna+1]
        Gy = imcinza[linha-1, coluna-1] * (-1) + imcinza[linha-1, coluna] * (-2) + \
             imcinza[linha-1, coluna+1] * (-1) + imcinza[linha+1, coluna-1] + \
             imcinza[linha+1, coluna] * 2 + imcinza[linha+1, coluna+1]
        
        criamatrizzero[linha, coluna] = math.sqrt(pow(Gx, 2) + pow(Gy, 2))

#Visualizem os resultados e salvem.
cv2.imshow('Imagem Sobel', criamatrizzero)
cv2.waitKey(0)

cv2.imwrite('Resultado com Sobel.jpg', criamatrizzero)









