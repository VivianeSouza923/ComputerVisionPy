#Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Apliquem os filtros passa baixa mediana (cv_median) e media (cv_blur), visualizem os resultados e salvem.Obs: busquem compreender os resultados de cada filtro.


import cv2

# primeiro pass: abrir uma imagem colorida. Como tu já sabe, pra abrir se utiliza a função imread eela vai receber como parametro o nome jpg da imagem salva no computador. VOu armazenar tudo isso em uma nova variável chamada x.
x = cv2.imread('pngtree-colorful-lattice-rainbow-background-image_110848.jpg')

# o segundo passo é transformar em tom de cinza. o meu cvtColor é quem fará isso e ela receberá 2 parametros: o arquivo da imagem que arquivamos na variável image no caso anterior e a função que de fato faz a transformação(COLOR_BGR2GRAY). TUDO ISSO VAI SER ARMAZENADO NA VARIÁVEL ABAIXO.
xcinza = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)

# terceiro passo visualizar imagem de entrada. Como já sabe, faço isso com a função imshow que recebe doiis parametros: na ordem, nome da janela e a variável onde está armazenada a imagem.
cv2.imshow('imagem de entrada.jpg', x)

#quarto passo: aplicar os filtros passa baixa mediana e media
cvmedian_x = cv2.medianBlur(xcinza, ksize=5) #mediana
cvblur_x = cv2.blur(xcinza, ksize=(5, 5)) #media



#quinto passo: visualizar o resultados.Como já sabe, faço isso com a função imshow que recebe doiis parametros: na ordem, nome da janela e a variável onde está armazenada a imagem (no caso, as imagens já filtradas).
cv2.imshow('Resultado do filtro passa baixa mediana', cvmedian_x)
cv2.imshow('Resultado do filtro passa baixa media', cvblur_x)

#por quanto tempo ficará na tela?
cv2.waitKey(0)

#sexto passo: vou salvar tudo que fizemos até aqui (última atualização). Quem faz isso? imwrite. Do que ele precisa para cumprit sua função? Dois parametros de entrada: o nome que vai ficar salvo no computador e a variável que recebeu todas as alterações que fiz. 
cv2.imwrite('resultado final com filtro passa baixa mediana.jpg', cvmedian_x)
cv2.imwrite('resultado final com filtro media.jpg', cvblur_x)
