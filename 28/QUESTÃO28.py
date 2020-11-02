#Abrir uma imagem colorida, transformar para tom de cinza e aplique e aplique a limiarização automática da própria Opencv, para que o limiar não dependa da aplicação e nem da luminosidade do local. Ahhh, então aqui a gente vai usar o cv2.adaptiveThreshold e não o cv2.threshold

#A assinatura do método é a seguinte: cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])

  #  src - array de origem (imagem)
  #  thresh - valor do limiar
  #  maxval - valor máximo
  #  type:
   #     cv2.ADAPTIVE_THRESH_MEAN_C : valor limite é a média da área dos vizinhos.
    #    cv2.ADAPTIVE*THRESH_GAUSSIAN_C : valor limite é a soma ponderada dos valores de vizinhança onde os pesos são uma janela gaussiana (tamanho do bloco x tamanho do bloco da posição x,y menos o valor C *(abaixo)_).
   # blockSize - tamanho do bloco dos vizinhos
    # C - É apenas uma constante que é subtraída da média ou da média ponderada calculada.

import cv2

#abrir uma imagem colorida
imcolor = cv2.imread('salada-completa-colorida-1.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)


#aplique a limiarização automática da própria Opencv
lim_aut = cv2.adaptiveThreshold(imcinza, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

#exibições
cv2.imshow('antes', imcinza)

cv2.imshow('limiarizada', lim_aut)
cv2.waitKey(0)
