#Após fazer a questão 42, gerem subimagens com cada objeto encontrado.

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

#pegar a forma da matriz/imagem
ls, cs = imcolor.shape[:2]

#desenhar blobs
for i, k in enumerate(blobs):

    #pegar as coordenas de cima-esquerda e baixo-direita
    x_ce = int(k.pt[0] - k.size)
    y_ce = int(k.pt[1] - k.size)

    x_bd = int(k.pt[0] + k.size)
    y_bd = int(k.pt[1] + k.size)


    #Verifique se essas coordenadas estão dentro dos limites da imagem, corrija se não estiver dentro dos limites

    if x_ce < 0:
        x_ce = 0
    if y_ce < 0:
        y_ce = 0

    if x_bd > cs:
        x_bd = cs
    if y_bd > ls:
        y_bd = ls

    #desenhar os retangulos agora. cv2.rectangle(imagem, onde começa as coordenas do retangulo, onde termina as coodenadas do retangulo, cor, espessura)
    #cv2.rectangle(imcolor, (x_ce + 15, y_ce + 15), (x_bd - 15, y_bd - 15), (0,255,0), 4)

    recorte = imcolor[y_ce + 15:y_bd - 15, x_ce + 15:x_bd - 15]

    cv2.imshow('Objeto'+ str(i+1), recorte)
    cv2.waitKey(10)

cv2.imshow('imagem em tom de cinza', imcinza)
cv2.waitKey(0)