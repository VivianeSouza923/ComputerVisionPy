#Abrir uma imagem colorida, transformar para tom de cinza e aplique a transformada de canny para detectar bordas. Apliquem o método cvFindContours para determinar quantos contornos existem na imagem. Apresentem o resultado obtido e a imagem de entrada. O retorno deve ser a mesma quantidade de objetos existentes.

import cv2
import numpy as np

#abrir uma imagem colorida
imcolor = cv2.imread('gelatina-colorida-camadas.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#aplique a transformada de canny para detectar bordas. O cv2.Canny recebe como parametros a imagem que se quer "cannyzar", o valor mínimo e o máximo.
imcanny =cv2.Canny(imcinza, 80, 180)

#descobrir quantos contornos existem na imagem
contornos, hierarquia = cv2.findContours(imcanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#vou fazer uma cópia da imagem original para poder fazer os contornos
cpimcanny = np.copy(imcolor)

#desenhar os contornos. A função cv2.drawContours recebe como parametros a imagem, os contornos existentes(que a gente descobriu duas linhas atrás), o -1 que é o índice de contornos (útil ao desenhar contornos individuais), a cor do contorno(no meu caso, eu botei verde) e a espessura
cv2.drawContours(cpimcanny, contornos, -1, (0, 255, 0), 5)

#mostrei a imagem de entrada
cv2.imshow('imagem de entrada', imcinza)

#mostrei o resultado obtido ao final de tudo
cv2.imshow('resultado obtido', cpimcanny)
cv2.waitKey(0)