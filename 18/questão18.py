#Abrir uma imagem colorida, transformar para tom de cinza e aplicar o operador gradiente Laplaciano, aplique a técnica de Equalização no resultado obtido na detecção das bordas, onde a maior intensidade de borda seja 255, e a menor intensidade da borda seja 0.

import cv2

#abrir uma imagem colorida
imcolor = cv2.imread('pngtree-colorful-grunge-paint-stain-set-png-image_3687008.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#visualizar imagem de entrada
cv2.imshow('visualizar', imcinza)
cv2.waitKey(0)

#aplicar o operador gradiente Laplaciano
l = cv2.Laplacian(imcinza, ddepth=cv2.CV_64F,ksize=3)

#conversão para uint8
l = cv2.convertScaleAbs(l)

cv2.imshow('visualizar L', l)
cv2.waitKey(0)

#equalização da imagem já filtrada por Laplacian
eql = cv2.equalizeHist(l)

cv2.imshow('visualizar eql', eql)
cv2.waitKey(0)




