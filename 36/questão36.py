#Abrir uma imagem colorida, transformar para tom de cinza e aplique a limiarização de otsu. Apliquem o método cvErode de forma iterativa, apresentando o resultado de cada iteração, verificando o que o método causa. O resultado deve ser diminuir as regiões brancas, então se o objeto for branco este método diminuirá o objeto.

import cv2
import numpy as np

#abrir uma imagem colorida
imcolor = cv2.imread('146c68a559359966c236d1ddbf4f13e7.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem em tom de cinza', imcinza)

#APLIQUE A LIMIARIZZAÇÃO DE OTSU. retval, dst=	cv.threshold(	src, thresh, maxval, type[, dst])
#parametros são, respectivamente, imagem, valor de limiarização, maáximo valor para ser usado com os tipos de limiarizaçao e por fim o tipo de limiarização.  
ret, imlim = cv2.threshold(imcinza, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('imagem limiarizada', imlim)

#Retorne um novo array de forma e tipo fornecidos, preenchido com uns.. Vamos fazer isso para usarmos logo em seguida. numpy.ones(shape, dtype=None, order='C') o dtype e order são opcionais. dtype: o tipo de dados desejados para a matriz
#onde (5,5) é a forma que estamos fornecendo a nova matriz e np.uint8 é o dtype
n_array = np.ones((5,5), np.uint8)

#pliquem o método cvErode de forma iterativa. o cv2.erode recebe como parametros a imagem limiarizada, o kernel que aqui está como n_array e o número de interações que serão i vezes.
for i in range(7):
    erode = cv2.erode(imlim, n_array, iterations=i)

    cv2. imshow('erodizada', erode)
    cv2.waitKey(1000)

