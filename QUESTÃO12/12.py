#Abram um arquivo de texto (pode ser o mesmo gerado no tópico 10), criem uma imagem em tom de cinza e visualizem esta imagem.

import cv2
import numpy as np

#ABRAM UM ARQUIVO DE TEXTO
arqtext = 'matriz.txt' #bom, aqui pra abrir eu vou guardar o arquivo de texto em uma variável
imagem = [] #lembre-se de que uma imagem é uma matriz

with open(arqtext, 'r') as infile: #'r' diz que estamos abrindo o arquivo para leitura, infile é o objeto de arquivo aberto a partir do qual leremos
    for i, line in enumerate(infile):
        linha = [int(number) for number in line.split()] #número inteiro para qualquer número da linha e isso será armazendao na variável linha que vamos utilizar para criar a imagem
        if i ==0:
            imagem = np.hstack(linha) #se estamos aqui pela primeira vez, temos que criar a primeira linha, certo? pra isso, utilizamos a np.hstack, mas ela só vai funcionar se nunca estivemos aqui porque ela não pode agir em diferente números de linhas. Lembre-se!

        else:
            imagem = np.vstack(([imagem, linha])) #se não estamos aqui a primeira vez, utilizamos a vstack. Por que? ela vai trazer diferentes linhas, ou seja, formar a matriz que é a imagem (não que a outra n forme, mas vai ser mais que uma linha)

final = np.asarray(imagem, np.uint8) #aqui eu vou fazer a conversão de ponto flutuante de 64 bits para uint8

#visualizem a esta imagem
cv2.imshow('visualizem esta imagem', final)
cv2.waitKey()



