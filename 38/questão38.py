#Faça o mesmo que a questão 37, alterando o elemento estruturante e sua referência e verifique o que acontece.

import cv2
import matplotlib.pyplot as plt

#abrir uma imagem colorida
imcolor = cv2.imread('xquadro-decorativo-pintura-sobre-tela-abstrato-colorido.jpg.pagespeed.ic.ZdIJjNvtuv.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem em tom de cinza', imcinza)

#aplique a limiarização de otsu. retval, dst=	cv.threshold(	src, thresh, maxval, type[, dst])
#parametros são, respectivamente, imagem, valor de limiarização, maáximo valor para ser usado com os tipos de limiarizaçao e por fim o tipo de limiarização.  
ret, imlim = cv2.threshold(imcinza, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('imagem limiarizada', imlim)

#cria um elemento estruturante
elemento_estruturante = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]

#aplicar a dilatação e mostrar os resultados para cada elemento estruturante
plt.figure(1)
titulos = ['Rectangular Kernel', 'Elliptical Kernel', 'Cross-shaped Kernel']
for i, elemento in enumerate(elemento_estruturante):
    n_array = cv2.getStructuringElement(elemento, (7,7))
    dilatação = cv2.dilate(imlim, n_array, iterations=i)

    win = 130 + (i+1)
    plt.subplot(win)
    plt.title(titulos[i])
    plt.imshow(dilatação, cmap='gray')

plt.show()
cv2.waitKey(0)