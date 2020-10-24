#Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Apliquem os filtros passa alta de canny (cv_canny), visualizem os resultados e salvem. Obs: busquem compreender os resultados do filtro.


import cv2

#primeiro passo: abrir uma imagem colorida
imcolor = cv2.imread('3.jpg')

#segundo passo: transformar em tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#TERCEIRO PASSO: VISUALIZAR IMAGEM DE ENTRADA
cv2.imshow('visualizar imagem de etrada', imcinza)

#aplicar o filtro passa alta de canny. O canny tá recebedo 3 parametros: a imagem já alterada pra ciza, o limirar 1 e o 2. 
canny_imcinza = cv2.Canny(imcinza, 80, 100)

#visualizzar os resultados
cv2.imshow('visualizar o resultado o Canny', canny_imcinza)

#por quanto tempo ficará aberta?
cv2.waitKey(0)

#por fim, vamos salvar tudo que fizemos
cv2.imwrite('RESULTADO.jpg', canny_imcinza)