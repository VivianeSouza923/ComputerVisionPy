#Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Apliquem um redimensionamento da imagem, reduzindo e depois aumentando seu tamanho, visualizem os resultados e salvem. Obs: uma imagem 320×240 deve virar uma 160×120 em primeiro caso e 640×480 em segundo caso.

import cv2

#primeiro passo: devo abrir uma imagem colorida. Para abrir uma imagem, eu devo criar uma variável(imcolor) e esta irá receber uma função chamada imread que terá com entrada uma imagem salva no meu computador. 
imcolor = cv2.imread('90.jpg')

#segundo passo}: transformar em tom de cinza. pARA ISSO, EU VOU CRIAR UMA VARIÁVEL(IMCINZA) E ELA IRÁ RECEBER A FUNÇÃO QUE CONVERTE A COR (CV2.CVTCOLOR) e essa função recebe dois parametros (a variavel que representa nossa imagem aberta, a função que transforma a imagem em cinza)
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#terceiro passo: visualizar imagem de entrada. para isso eu vou utilizar a função imshow e ela terá dois parametros de entrada: o nome da janela que será aberta quando o meu código rodar e a variavel que contém a imagem transformada em cinza
cv2.imshow('visualizar imagem de entrada', imcinza)

#quarto passo: aplicarcar um redimensionamento de imagem. Primeiramente, a gente tem que pegar a foram das linhas e colunas. Como fazer isto? Criei duas variáreis para linhas e colunas e elas vão receber a função shape (forma) e vai ser [:2], uma vez que o enunciado pede o dobro e metade.
linhas, colunas = imcinza.shape[:2]

#quinto passo: reduzinndo pela metade os pixels das linhas e colunas. Como fiz? Criei uma variável e ela vai receber a função resize que recebe como parametros: imcinza (nossa imagem), alteração que eu quero fazer nas linhas e colunas dela
reduzir_imcinza = cv2.resize(imcinza, (int(linhas/2), int(colunas/2)))

#sexto passo: dobrar os pixels da linhas e colunas. Como fiz? Criei uma variável e ela vai receber a função resize que recebe como parametros: imcinza (nossa imagem), alteração que eu quero fazer nas linhas e colunas dela
aumentar_imcinza = cv2.resize(imcinza, (2*linhas, 2*colunas))

#sétimo passo: visualizar os resultados. para tanto utilizo a função imshow que recebe dois parametros: o nome da janela e o resultado do passo anterior (redução ou aumento)
cv2.imshow('imagem reduzida', reduzir_imcinza)
cv2.imshow('imagem aumentada', aumentar_imcinza)

cv2.waitKey(0)

#oitavo passo: salvar os resultados. Como salvo? função imwrite que receve 2 parametros: o nome que ficará salvo no computador e o arquivo alterado que eu quero deixar salvo
cv2.imwrite('imagem_reduzida.jpg', reduzir_imcinza)
cv2.imwrite('imagem_aumentada.jpg', aumentar_imcinza)

