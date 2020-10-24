#Abrir uma imagem colorida, transformar para tom de cinza e aplicar o operador gradiente Sobel, visualizando a imagem de entrada e seu respectivo histograma inicialmente, e, em seguida, o resultado do operador gradiente e seu histograma. Esta técnica realça melhor as bordas da imagem.

import cv2
import math 
import matplotlib.pyplot as plt

#abrir uma imagem colorida
imcolor = cv2.imread('ec6a342ad967ce4927fad57dac0c0379-fundo-de-respingo-de-tinta-colorida.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#APLICAR O OPERADOR GRADIENTE SOBEL
Gx = cv2.Sobel(imcinza, dx=1, dy=0, ddepth=cv2.CV_64F, ksize=3)
Gy = cv2.Sobel(imcinza, dx=0, dy=1, ddepth=cv2.CV_64F, ksize=3)

S = (Gx**2 + Gy**2)**(1/2)

#sempre precisa fazer a conversão para uint8!!!!!!!!!!!
S = cv2.convertScaleAbs(S)

#EXIBIÇÃO
plt.figure(1)
plt.subplot(221)
plt.imshow(imcinza, cmap='gray')
plt.subplot(222)
plt.hist(imcinza.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(S, cmap='gray')
plt.subplot(224)
plt.hist(S.ravel(), 256, [0, 256])
plt.show()
