#Abrir uma imagem colorida, transformar para tom de cinza e aplicar uma Equalização de histograma utilizando apenas o conhecimento de manipulação da imagem, sem a OpenCv, visualizando a imagem de entrada e seu respectivo histograma inicialmente, e, em seguida, o resultado da equalização e seu histograma. Esta técnica aumenta o contraste da imagem.

import cv2
import numpy as np
import matplotlib.pyplot as plt

#abrir uma imagem colorida
imcolor = cv2.imread('11550326_nino-rocha-fotografia-653.jpg')

#transformar para tom e cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

orihist = np.zeros([256], np.uint8)
eqhist = np.zeros([256], np.uint8)

ls, cs = imcinza.shape[:2]

x = imcinza.flatten()

for pixel in x:
    orihist[pixel] += 1


# Calculates the cumulative distribution function of the histogram
w = [sum(orihist[:i + 1]) for i in range(len(orihist))]
w = np.array(w)

#NNormalize o w para estar entre 0-255
n_w = ((w - w.min())*255)/(w.max() - w.min())
n_w = n_w.astype('uint8')

eqim = n_w[x]
eqim = np.reshape(eqim, imcinza.shape)

plt.figure(1)
plt.subplot(221)
plt.imshow(imcinza, cmap='gray')
plt.subplot(222)
plt.hist(imcinza.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(eqim, cmap='gray')
plt.subplot(224)
plt.hist(eqim.ravel(), 256, [0, 256])
plt.show()
