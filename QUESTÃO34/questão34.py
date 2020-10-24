#Verificar se está ocorrendo acumulo de memória a cada iteração, aprendendo a apagar cada objeto quando não usar mais os mesmos.

import cv2
import numpy as np

#abrir uma imagem colorida
imcolor = cv2.imread('b.png')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#fazer uma cópia da imagem original para começar a desenhar os retÂngulos
cp_imcolor = np.copy(imcolor)

del imcolor

#aplicar a transformada de canny. cv2.Canny recebe como parametros a imagem, o valor mínimo e máximo
imcanny = cv2.Canny(imcinza, 80, 180)

#descobrir quantos contornos existem na imagem
contornos, hierarquia = cv2.findContours(imcanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

del imcanny, hierarquia

#encontrar uma aproximação de polígono para cada contorno
contours_poly = [None] * len(contornos)

#encontrar o retângulo limitado para cada polígono
bound_rect = [None] * len(contornos)

#cv2.approxPolyDP(curve, epsilon, closed[, approxCurve]) ONDE CURVE É Vetor de entrada de um ponto 2D armazenado em std :: vector ou Mat, EPSILON É Parâmetro que especifica a precisão da aproximação. Esta é a distância máxima entre a curva original e sua aproximação E CLOSED VAI RECEBER TRUE OU FALSE Se verdadeiro, a curva aproximada é fechada (seu primeiro e último vértices são conectados). Caso contrário, não está fechado.
for i, contorno in enumerate(contornos):
    contours_poly[i] = cv2.approxPolyDP(contorno, 2, True)
    bound_rect[i] = cv2.boundingRect(contours_poly[i])



#vou desenhar para cada i, contorno um retângulo. cv2.rectangle(image, start_point, end_point, color, thickness)onde image é a imagem onde a gente vai desenha-los, start_point é onde se inicia as coordenadas do retângulo, end_point é onde acaba as coordenadas do retângulo color é a cor e thickness é a espessura
for i, contorno in enumerate(contours_poly):
    cv2.rectangle(cp_imcolor, (int(bound_rect[i][0]), int(bound_rect[i][1])),
                  (int(bound_rect[i][0]) + int(bound_rect[i][2]), int(bound_rect[i][1]) + bound_rect[i][3]),
                  (255, 0, 0), 2)


    #fazendo o recorte de cada contorno/retângulo agora
    sub_im = cp_imcolor[int(bound_rect[i][1]):int(bound_rect[i][1]) + bound_rect[i][3],
                       int(bound_rect[i][0]):int(bound_rect[i][0]) + int(bound_rect[i][2])]

    #mostrar cada recorte que eu fiz
    cv2.imshow('subimagem' + str(i+1) + ':', sub_im)
    cv2.waitKey(10)

    del sub_im

#mostar a imagem de entrada
cv2.imshow('entrada', imcinza)

del imcinza

#mostrar o resultado final
cv2.imshow('final', cp_imcolor)
cv2.waitKey(0)
