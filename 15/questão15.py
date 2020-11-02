#Abrir uma câmera, capturar uma imagem (frame), transforme em tom de cinza, visualizar imagem de entrada, aplique o filtro de canny e visualize os resultados. Continue infinitamente capturando, transformando em tom de cinza, aplicando canny e visualizando.

import cv2

#Abrir uma câmera
ac = cv2.VideoCapture(0)

while 1:
    #capturar uma imagem(frame)
    ret, infini = ac.read()

    #transformar em tom de cinza
    imcinza = cv2.cvtColor(infini, cv2.COLOR_BGR2GRAY)

    #aplicar o filtrp de canny
    canny = cv2.Canny(imcinza, 30, 100)

    #visualizando
    cv2.imshow('visualizando', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'): #condição para o loop parar
        break     

