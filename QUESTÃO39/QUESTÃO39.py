#Abrir uma imagem colorida, transformar para tom de cinza e aplique a limiarização de otsu. Apliquem o método cvErode de forma iterativa, apresentando o resultado de cada iteração, verificando o que o método causa. Utilize um elemento estruturante com uma linha e três colunas, com a referencia no centro, então o objeto deve diminuir apenas na vertical, pois o elemento estruturante é vertical. O objeto deve ser branco e o fundo preto.

import cv2

#abrir uma imagem colorida
imcolor = cv2.imread('4c66bbf0ef9et.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem transformada para tom de cinza', imcinza)

#aplique a limiarização de otsu. retval, dst=	cv.threshold(	src, thresh, maxval, type[, dst])
#parametros são, respectivamente, imagem, valor de limiarização, maáximo valor para ser usado com os tipos de limiarizaçao e por fim o tipo de limiarização.  
ret, imlim = cv2.threshold(imcinza, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('imagem limiarizada por otsu', imlim)

#Utilize um elemento estruturante com uma linha e três colunas, com a referencia no centro, então o objeto deve diminuir apenas na vertical, pois o elemento estruturante é vertical.
n_array = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))

#Apliquem o método cvErode de forma iterativa, apresentando o resultado de cada iteração
for i in range(9):
    erode = cv2.erode(imlim, n_array,iterations=i)

    cv2.imshow('imagem erodizzada', erode)
    cv2.waitKey(1000)




