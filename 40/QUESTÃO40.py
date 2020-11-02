#Faça o mesmo que a questão 39, alterando o elemento estruturante e sua referência e verifique o que acontece.

import cv2
import matplotlib.pyplot as plt

#abrir uma imagem colorida
imcolor = cv2.imread('maca-do-amor-colorida.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem transformada para tom de cinza', imcinza)

#aplique a limiarização de otsu. retval, dst=	cv.threshold(	src, thresh, maxval, type[, dst])
#parametros são, respectivamente, imagem, valor de limiarização, maáximo valor para ser usado com os tipos de limiarizaçao e por fim o tipo de limiarização.  
ret, imlim = cv2.threshold(imcinza, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('imagem limiarizada por otsu', imlim)

#cria um elemento estruturante
elemento_estruturante = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]

#aplicar a erosão e mostrar os resultados para cada elemento estruturante
plt.figure(1)
titulos = ['Rectangular Kernel', 'Elliptical Kernel', 'Cross-shaped Kernel']
for i, elemento in enumerate(elemento_estruturante):
    n_array = cv2.getStructuringElement(elemento, (5,5))
    erosão = cv2.erode(imlim, n_array, iterations=i)

    win = 130 + (i+1)
    plt.subplot(win)
    plt.title(titulos[i])
    plt.imshow(erosão, cmap='gray')

plt.show()
cv2.waitKey(0)
    