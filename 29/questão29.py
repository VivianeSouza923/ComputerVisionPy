#Abrir uma imagem colorida, transformar para tom de cinza e aplique a transformada de hough para detectar bordas. Faça um desenho no paint que contenha diversos objetos, inclusive um círculo e apenas o círculo deve ser detectado.

#circles = cv.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]] )

# image: imagem 8-bit, monocanal, imagem de entrada em escala de cinza.

   # method: Método de detecção. Atualmente, o único método implementado é HOUGH_GRADIENT.

    # dp: Relação inversa entre a resolução do acumulador e a resolução da imagem. Por exemplo, se dp=1 , o acumulador tem a mesma resolução que a imagem de entrada. Se dp=2 , o acumulador tem a metade da largura e altura.

   #  minDist: Distância mínima entre os centros dos círculos detectados. Se o parâmetro for muito pequeno, vários círculos vizinhos podem ser detectados falsamente, além do verdadeiro. Se for muito grande, alguns círculos podem não ser detectados.

   # param1: Primeiro parâmetro específico do método. No caso do HOUGH_GRADIENT , é o limiar mais alto dos dois passados para o detector de arestas Canny (o mais baixo é duas vezes menor).

  #  param2: Segundo parâmetro específico do método. No caso do HOUGH_GRADIENT , é o limiar do acumulador para os centros do círculo na fase de detecção. Quanto menor for, mais falsos círculos podem ser detectados. Os círculos, correspondentes aos valores maiores do acumulador, serão retornados primeiro.

  #  minRadius: Raio mínimo do círculo.

   # maxRadius: Raio máximo do circulo. Se = 0, utiliza a dimensão máxima da imagem. Se < 0, devolve os centros sem encontrar o raio.


import cv2
import numpy as np

#abrir uma imagem colorida
imcolor = cv2.imread('image.png')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#aplique a transformada de hough para detectar bordas
circles = cv2.HoughCircles(imcinza, cv2.HOUGH_GRADIENT, 1, 30, param1 = 150, param2 = 25, minRadius = 0, maxRadius = 0)


#tente 
try:
    #arredonar uniformente os valores da matriz do mesmo tipo que circles. O arredondamento será feito em números inteiros, sem sinal de 0 a 65535 (np.uint16 faz essa limitação)
    circles = np.uint16(np.around(circles))
#caso a tentativa falhe, vou imprimir mensagem de erro
except AttributeError:
    print('None circles found! Try change the parameters.')
    exit()

#criar uma cópia da imagem original para desenhar os círculos
circles_n = np.copy(imcolor)

#desenhe todos os circulos encontrados  
for xc, yc, radius in circles[0, :]:
    cv2.circle(circles_n, (xc, yc), radius, (0, 255, 0), 2)

#mostrar a imagem de entrada (que é a que só recebeu o tom de cinza)
cv2.imshow('entrada', imcinza)

#mostrar o resultado final com os círculos desenhados
cv2.imshow('final', circles_n)
cv2.waitKey(0)



