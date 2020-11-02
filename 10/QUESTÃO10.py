#Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows), peguem cada um dos pixels da imagem e coloquem na matriz que criaram. Apliquem uma limiarização fazendo uma varredura na matriz. Imprimam esta matriz em um arquivo de texto (*.txt) do mesmo modo que ela está alocada.

import cv2
import numpy as np #vou precisar dessa biblio pra azer a matriz de zeros. Lembre-se disso.

#primeiro passo: abrir uma imagem colorida
imcolor = cv2.imread('dori_mari_26.05.111.jpg')

#segundo passo: transformar em tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#terceiro passo: visualizar imagem de entrada
cv2.imshow('visualizar imagem de entrada', imcinza)
cv2.waitKey(0)

#quarto passo: criari uma matrix de forma estática com as mesmas dimensões da imagem de entrada, mas antes disso vamos pegar o shape da foto
ls, cs = imcinza.shape[:2]

#quinto passo: criar uma matriz de zeros para a limiarização
thMatriz = np.zeros((ls, cs), dtype=np.uint8)

for l in range(ls): #para cada linha das ls nós vamos verificar a coluna
    for c in range(cs): #para cada coluna das cs, nós vamos fazer o que manda na linha abbaixo
        thMatriz[l, c] = imcinza[l, c] #nossa thMatriz vai receber os valores da matriz imcinza


#sexo passo: vamos preencher a matriz com os limites de limiarização
with open('matriz.txt', 'w') as outfile:
    for l in range(ls): #para cada linha das ls nós vamos verificar a coluna
        for c in range(cs): #para cada coluna das cs, nós vamos fazer o que manda na linha abbaixo
            if thMatriz[l, c] < 127:
                thMatriz[l, c] = 0
            else:
                thMatriz[l, c] = 255 #ou seja, em resumo, só vou ter 0 ou 255 na minha matriz (isso foi possívelpor causa da minha limiarização)

            outfile.write(str(thMatriz[l, c]) + ' ')
        outfile.write('\n')


