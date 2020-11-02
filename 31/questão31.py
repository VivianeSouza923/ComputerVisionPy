#Após fazer a questão 30, destaque cada objeto encontrado desenhando um retângulo indicando onde os mesmos se encontram. Utilizar a função “cvContourBoundingRect” para determinar cada contorno. Ressalto que é necessário percorrer os contornos encontrados na função “cvFindContours” de forma correta.

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

#Encontre uma aproximação de polígono para cada contorno
contours_poly = [None] * len(contornos)

#encontre o retângulo limitado para cada polígono
bound_rect = [None] * len(contornos)

#cv2.approxPolyDP(curve, epsilon, closed[, approxCurve]) ONDE CURVE É Vetor de entrada de um ponto 2D armazenado em std :: vector ou Mat, EPSILON É Parâmetro que especifica a precisão da aproximação. Esta é a distância máxima entre a curva original e sua aproximação E CLOSED VAI RECEBER TRUE OU FALSE Se verdadeiro, a curva aproximada é fechada (seu primeiro e último vértices são conectados). Caso contrário, não está fechado.
for i, contorno in enumerate(contornos):
    contours_poly[i] = cv2.approxPolyDP(contorno, 2, True) 
    bound_rect[i] = cv2.boundingRect(contours_poly[i])

#criar a cópia da imagem para fazer os contornos
cp_imcolor = np.copy(imcolor)

#desenhando os retangulos. cv2.rectangle(image, start_point, end_point, color, thickness)onde image é a imagem onde a gente vai desenha-los, start_point é onde se inicia as coordenadas do retângulo, end_point é onde acaba as coordenadas do retângulo color é a cor e thickness é a espessura
for i, contorno in enumerate(contours_poly):
    cv2.rectangle(cp_imcolor, (int(bound_rect[i][0]), int(bound_rect[i][1])),
                  (int(bound_rect[i][0]) + int(bound_rect[i][2]), int(bound_rect[i][1]) + bound_rect[i][3]),
                  (0, 0, 255), 2)

cv2.imshow('entrada', imcinza)

cv2.imshow('final', cp_imcolor)
cv2.waitKey(0)


