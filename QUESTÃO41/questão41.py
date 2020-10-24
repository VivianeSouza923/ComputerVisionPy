#Abrir uma imagem colorida, transformar para tom de cinza e aplique a transformada de canny para detectar bordas. Apliquem a biblioteca “blob” para determinar quantos contornos existem na imagem. Apresentem o resultado obtido e a imagem de entrada. O retorno deve ser a mesma quantidade de objetos existentes.

import cv2

#abrir uma imagem colorida
imcolor = cv2.imread('b.png')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#aplique a transformada de canny para detectar bordas
imcanny = cv2.Canny(imcinza, 80, 100)

#Apliquem a biblioteca “blob” para determinar quantos contornos existem na imagem.

#defina os parametros
params = cv2.SimpleBlobDetector_Params()

#filtre por área
params.filterByArea = True
params.minArea = 20
params.maxArea = 40000

#filtrar por circularidade
params.filterByCircularity = False
params.minCircularity = 0.1

#filtrar por convexidade
params.filterByConvexity = False
params.minConvexity = 0.87

#filtrar or inercia 
params.filterByInertia = False
params.minInertiaRatio = 0.8

#distância entre blobs 
params.minDistBetweenBlobs = 20

#criar um blob detector com os parametros
detector = cv2.SimpleBlobDetector_create(params)

#detectar os objetos na imagem limiarizada
blobs = detector.detect(imcanny)

#apresentem o resultado obtido. Imprime quantos objetos estão na imagem
print(len(blobs))

cv2.imshow('imagem em tom de cinza', imcinza)
cv2.waitKey(0)

