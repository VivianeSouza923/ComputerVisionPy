#Abrir uma câmera, capturar uma imagem (frame), transforme em tom de cinza, visualizar imagem de entrada. Continue infinitamente capturando, transformando em tom de cinza e vizualizando.

import cv2

#Abrir uma câmera, capturar uma imagem (frame)
ac = cv2.VideoCapture(0) #autoexplicativa

while 1:
    ret, infini = ac.read() #a leitura da captura de vídeo está sendo armazenada na variável para então podermos dar o tom de cinza

    imcinza = cv2.cvtColor(infini, cv2.COLOR_BGR2GRAY) #dando tom de cinza

    cv2.imshow('visualizar', imcinza) #visualizando a imagem já em cinza.

    if cv2.waitKey(1) & 0xFF == ord('q'): #apertando a letra q no teclado, o loop chega ao fim, se isso nunca acontecer, a câmera p&b ficará aberta para todo o sempre
        break 





