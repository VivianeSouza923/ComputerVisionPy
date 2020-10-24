#Abrir uma imagem colorida, transformar para tom de cinza e aplicar uma Equalização de histograma utilizando a OpenCv, visualizando a imagem de entrada e seu respectivo histograma inicialmente, e, em seguida, o resultado da equalização e seu histograma. Esta técnica aumenta o contraste da imagem.


import cv2
import matplotlib.pyplot as plt

#Abrir uma imagem colorida
imcolor = cv2.imread('notas-musicais-coloridas-13308552.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#EQUALIZAR A IMAGEM
eq = cv2.equalizeHist(imcinza)

#histograma da imagem original
orihist = cv2.calcHist(imcinza, channels=[0], mask=None, histSize=[256], ranges=[0,256])

#histograma da imagem equalizada
eqhist = cv2.calcHist(eq, channels=[0], mask=None, histSize=[256], ranges=[0,256])

plt.figure(1)
plt.subplot(221)
plt.imshow(imcinza, cmap='gray') #mostra a imagem
plt.subplot(222)
plt.hist(imcinza.ravel(), 256, [0, 256]) #mostra o gráfico de fato
plt.subplot(223)
plt.imshow(eq, cmap='gray') #mostra a imagem
plt.subplot(224)
plt.hist(eq.ravel(), 256, [0, 256]) #mostra o gráfico de fato
plt.show()
