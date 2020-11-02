#Após fazer a questão 31, calcule a área de cada contorno obtido através da função “cvContourArea”, apresentando seu valor.

import cv2
import numpy as np

#abrir uma imagem colorida
imcolor = cv2.imread('b.png')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#aplique a transformada de canny para detectar bordas. O cv2.Canny recebe como parametros a imagem que se quer "cannyzar", o valor mínimo e o máximo.
imcanny =cv2.Canny(imcinza, 80, 180)

#descobrir quantos contornos existem na imagem
contornos, hierarquia = cv2.findContours(imcanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print (hierarquia)

#fazer a cópia da imagem original para que a gente possa desenhar os contornos nela
cp_imcolor = np.copy(imcolor)

#desenhando os contornos
cv2.drawContours(cp_imcolor, contornos, -1, (255, 0, 0), 5)

#cálculo da área do contorno
for i, contorno in enumerate(contornos):
    print('Area' + str(i+1) + ':' + str(cv2.contourArea(contorno)))

cv2.imshow('entrada', imcinza)

cv2.imshow('final', cp_imcolor)
cv2.waitKey(0)


