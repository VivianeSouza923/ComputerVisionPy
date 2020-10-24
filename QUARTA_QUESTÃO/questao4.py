#Abrir uma imagem colorida, transformar em HSV, visualizar e salvar cada um dos canais separadamente. Obs: Busquem compreender o que significa cada um dos canais.

 #Lembre-se do que é uma imagem em HSV: H É A TONALIDADE, OU SEJA, VERMELHO, AZUL ETC. S É A SATURAÇÃO: MAIS FRIO OU QUENTE. QUANTO MENOR O VALOR, MAIS CINZA VAI APARECER. QUANTO MAISO O VALOR, MAIS PURA ELA VAI SER, OU SEJA, MAIS PERTO DO NORMAL (DIGAMOS ASSIM). POR FIM, O V É O BRILHO (AUTOEXPLICATIVO NÉ)

import cv2

# primeiro passo: abrir uma imagem colorida. VOu abrir usando a função imread e o resultado será atribuído à variável image.
image = cv2.imread('9.jpg')

# segundo passo: transformar em HSV. Como tu faz isso? pega a função cvtColor e ela terá como entrada o resultado do primeiro passo e a função COLOR_BGR2HSV(NOTE QUE PARA AS 3 ÚLTIMAS LETRAS MUDARAM DO EXEMPLO DO CINZA). o RESULTADO DA FUNÇÃO cvtColor será atribuída à variável hsv_image.  
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# o terceiro passo: eu vou ter que dividir o meu hsv, ou seja, um arquivo terá só o h, o outro s etc. Para isso, eu estou usando a minha função split que tem como parametro o resultado do segundo passo, ou seja a imagem em HSV. 
h, s, v = cv2.split(hsv_image)

# aqui eu vou visualizar a imagem em HSV. Uso a função imshow e ela tem como parametros o nome do quadro (da janela que vai abrir quando eu compilar o código e a minha imagem trasformada em HSV)
cv2.imshow('HSV Image', hsv_image)

#AQUI NA PRIMEIRA LINHA EU VOU VISUALIZAR A IMAGEM SÓ COM O H (TONALIDADE), NA SEGUNDA SÓ O S (SATURAÇÃO) E NA TERCEIRA SÓ COM O V (BRILHO). VOCÊ TÁ MOSTRRANDO SEPARADAMENTE, VIVIANE. COMO VOCÊ JÁ SABE, O IMSHOW RECEBE OS DOIS PARAMETROS: O NOME QUE VAI FICAR NA JANELA E A VARIÁVEL QUE CONTEM O QUE A GENTE QUER VER
cv2.imshow('H Channel', h)
cv2.imshow('S Channel', s)
cv2.imshow('V Channel', v)


#A JANELA VAI SUMIR EM QUANTO TEMPO?
cv2.waitKey(0)

# COMO JÁ SABE, MAS N CUSTA LEMBRAR... AQUI A GENTE VAI SALVAR O QUE A GENTE VIU NO PASSO ANTERIOR. OU SEJA, SALVO A MINHA IMAGEM EM HSV, H, S E V. PARA ISSO, TÔ UTILIZANDO A FUNÇÃO IMWRITE E ELA RECEBE COMO PARAMETRO: O NOME QUE EU ESCOLHI PRA SALVAR E A VARIÁVEL.
cv2.imwrite('hsv_image.jpg', hsv_image)
cv2.imwrite('h_channel.jpg', h)
cv2.imwrite('s_channel.jpg', s)
cv2.imwrite('v_channel.jpg', v)
