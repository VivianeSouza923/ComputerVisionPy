#Abrir uma imagem colorida, transformar em níveis de cinza, visualizar e salvar imagem gerada.

import cv2

imcolor = cv2.imread('a.jpg')

imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

cv2.imshow('visualizar', imcinza)
cv2.waitKey(0)

cv2.imwrite('resultado.jpg', imcinza)