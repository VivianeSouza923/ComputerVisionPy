#Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Apliquem uma limiarização (thresholding), visualizem os resultados e salvem. Obs: busquem compreender os resultados da técnica.


import cv2

#primeiro passo = abrir uma imagem colorida. Como faço? Utilizo a função imread (ela recebe um parametro que é a imagem que eu salvei no computador)e vou atribui-la à variável imcolor. 
imcolor = cv2.imread('cores.jpg')

#segundo passo = transformar em tom de cinza. Como faço? crio uma variavel e a ela vou atribuir a função cvtColor que recebe como parametro a imcolor e a função de fato cinza (COLOR_BGR2GRAY)
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#TERCEIRO PASSO = VISUALIZAR IMAGEM DE ENTRADA
cv2.imshow('visualizar imagem de entrada', imcinza)

#quarto passo = aplicar uma limiarização
ret, imcolor_threshold = cv2.threshold(imcinza, 70, 255, cv2.THRESH_BINARY)

#QUINTO PASSO = VISUALIZAR O RESULTADO
cv2.imshow('visualizar resultado', imcolor_threshold)

cv2.waitKey(0)

#salvar o resultado
cv2.imwrite('resultado_salvo.jpg', imcolor_threshold)
