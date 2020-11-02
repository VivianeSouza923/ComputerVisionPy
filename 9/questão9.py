#-Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows), peguem cada um dos pixels da imagem e coloquem na matriz que criaram. Imprimam esta matriz em um arquivo de texto (*.txt) do mesmo modo que ela está alocada.

import cv2

#primeiro passo: abrir uma imagem colorida
imcolor = cv2.imread('d.jpg')

#segundo passo: transformar em tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#TERCEIRO PASSO: VISUALIZAR IMAGEM DE ENTRADA
cv2.imshow('visualizar imagem de entrada', imcinza)
cv2.waitKey(0)

#vamo pegar a forma das linhas e colunas primeiro. criei as variáveis linhas, colunas e atribuí a elas a forma de imcinza. vemos que a foto é 300x300. lados são igualmente proporcionais.
linhas, colunas = imcinza.shape[:2]

#quinto passo: criar uma matriz de forma estática com as mesmas dimensões da imagem de entrada
with open('matriz.txt', 'w') as outfile: #o arquivo aberto vamos começar a preencher
    for linha in range(linhas): #para cada linha dentro da variável linhas a gente verifica as colunas
        for coluna in range(colunas): #para cada coluna da variável colunas a gente vai começar a preencher
            outfile.write(str(imcinza[linha, coluna]) + '  ') #o arqquivo será preenchido com o valor do pixel de ij (linhacoluna) + um espaço e se a linha ainda não foi preenchida ele volta para a for coluna... caso tenha sido, ele pula linha (write da linha abaixo) e vai para o for linha...
        outfile.write('\n')