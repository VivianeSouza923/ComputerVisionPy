#Abrir uma imagem colorida em RGB, visualizar e salvar cada um dos canais separadamente. Obs: Busquem compreender o que significa cada um dos canais.


import cv2

# PRIMEIRO PASSO: ABRIR UMA IMAGEM COLORIDA. MEU IMREAD FARÁ ISSO E VAI COLOCAR DENTRO DA VARIÁVEL IMAGE.
image = cv2.imread('rgb.jpg')

# SEPARAR CADA UNS DOS CANAIS, OU SEJA, O AZUL, VERDE E VERMELHO (FORMAM O SISTEMA RGB DE CORES DAS FOTOS). A FUNÇÃO SPLIT FARÁ A DIVISÃO.
blue_channel, green_channel, red_channel = cv2.split(image)

# MOSTRAR SEPARADAMENTE CADA UM DOS CANAIS. OBSERVE QUE AO MOSTRAR O CANAL DESEJADO, ONDE TEM A COR DELE FICARÁ BRANCO E O RESTO PRETO..
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

cv2.waitKey(0)

# Vamos salvar separadamente os resultados obtidos do passo anterior
cv2.imwrite('blue_channel.jpg', blue_channel)
cv2.imwrite('green_channel.jpg', green_channel)
cv2.imwrite('red_channel.jpg', red_channel)