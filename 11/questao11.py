#Abrir uma imagem colorida com o fundo branco e um quadrado preto centralizado, transformar em tom de cinza, visualizar imagem de entrada. Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows), peguem cada um dos pixels da imagem e coloquem na matriz que criaram. Calculem as coordenadas (xc,yc) que representam o centróide deste quadrado. Tentem pintar ou marcar ele na imagem para visualização. Xc será a média todas as coordenadas x que fazem parte do quadrado, e yc é as médias de y do quadrado. As coordenadas do quadrado são identificadas pelo tom preto(valor 0). Façam esta imagem de entrada no Paint.

import cv2
import numpy as np 

#passo 1: abrir uma imagem colorida o fundo branco e um quadrado preto centralizado
imcolor = cv2.imread('ge.jpg')

#passo 2: TTRANSFORMAR EM TOM DE CINZA
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#PASSO 3: VISUALIZAR IMAGEM DE ENTRADA
cv2.imshow('visualizar iagem de entrada', imcinza)

#passo 4: Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows), peguem cada um dos pixels da imagem e coloquem na matriz que criaram.

#primeiro pega o shape da imagem 
ls, cs = imcinza.shape[:2]

#cria uma matriz de zeros. Eu vou usar pra receber a matriz da imagem em tom de cinza
mazero = np.zeros((ls, cs), dtype=np.uint8)

#mazero recebe a matriz de tom de cinza
for l in range(ls):
    for c in range(cs):
        mazero[l, c] = imcinza [l, c]

#passo 5: Calculem as coordenadas (xc,yc) que representam o centróide deste quadrado.

#inicializa as variáveis
x0 = 0
y0 = 0
cont = 0

#nesse laço eu vou percorrer todo o quadrado, ateé chegar no xf, yf (ou seja, até o último pixel)
for l in range(ls):
    for c in range(cs):
        if imcinza[l, c] == 0: #As coordenadas do quadrado são identificadas pelo tom preto(valor 0).
            x0 += l
            y0 += c
            cont += 1

#percorri todo o quadrado, mas o centro dele (x0, y0) vai ser dito agora
x0 = int(x0/cont)
y0 = int(y0/cont)

#passo 6: marcação da centróide. Vamos marcar com um circulo
cv2.circle(mazero, (x0, y0), 7, (255, 255, 255), -1 ) #cv2.circle (imagem, coordenadas_centrais, raio, cor, espessura) #Espessura de -1 px preencherá a forma do círculo com a cor especificada.

#mostra o resultado
cv2.imshow('mostra o resultado', mazero)
cv2.waitKey(0)

#salvando todas as alterações
cv2.imwrite('rsultado.jpg', mazero)


