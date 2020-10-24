#Faça o mesmo que a questão 25, entretanto apenas forneça a imagem de entrada, detecte quantos objetos existem de forma automática, rotulando cada região de forma automática, e no final apresente cada objeto encontrado por uma cor distinta.

import cv2
import numpy as np
import random

#Faça o mesmo que a questão 25, entretanto apenas forneça a imagem de entrada
def CR(imcolor):

    #pegar a forma da imagem/matriz
    ls, cs = imcolor.shape[:2]

    #criar a matriz de zeros que terá a mesma forma e elementos de imcolor
    matrizzero = np.zeros_like(imcolor)

    #Crie uma variável para armazenar o número de objetos encontrados
    object_found = 0

    #encontrar os objetos
    for ext_l in range(ls):
        for ext_c in range(cs):
            if matrizzero[ext_l, ext_c] == 0 and imcolor[ext_l, ext_c] < 230:
                object_found+=1
                matrizzero[ext_l, ext_c] = object_found

                #inicializa as variáveis de comparação e incrementação para percorrer a imagem até que a região pare de crescer
                cf = 0
                pp = 1

                #enquanto as variáveis forem diferentes a região vai crescer
                while pp != cf:
                    pp = cf
                    cf = 0

                    #percorrer a linhas de cada coluna para fazer a região crescer
                    for l in range(ls):
                        for c in range(cs):
                            if matrizzero[l, c] == object_found:
                                if imcolor[l-1, c-1] < 230:
                                    matrizzero[l-1, c-1] = object_found
                                    cf+=1
                                if imcolor[l-1, c] < 230:
                                    matrizzero[l-1, c] = object_found
                                    cf+=1
                                if imcolor[l-1, c+1] < 230:
                                    matrizzero[l-1, c+1] = object_found
                                    cf+=1
                                if imcolor[l, c-1] < 230:
                                    matrizzero[l, c-1] = object_found
                                    cf+=1
                                if imcolor[l, c+1] < 230:
                                    matrizzero[l, c+1] = object_found
                                    cf+=1
                                if imcolor[l+1, c-1] < 230:
                                    matrizzero[l+1, c-1] = object_found
                                    cf+=1
                                if imcolor[l+1, c] < 230:
                                    matrizzero[l+1, c] = object_found
                                    cf+=1
                                if imcolor[l+1, c+1] < 230:
                                    matrizzero[l+1, c+1] = object_found
                                    cf+=1
    
    return matrizzero, object_found

#leitura e exibição

if __name__ == '__main__':

    #abrir a imagem colorida
    imcolor = cv2.imread('image.jpg')

    #transformar pra tom de cinza
    imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

    #mostrar o resultado da imagem após a aplicação do tom de cinza
    cv2.imshow('imagem cinza', imcinza)

    #armazenar a plicação de crescimento de regiões na imagem na imagem segmentada e objetos encontrados
    imseg, os = CR(imcinza)

    #criar a matriz de cores. Primeiro pegaa forma da matriz da imagem segmentada e em seguida vamos criar uma matriz coma mesma forma e elementos dela

    ls, cs = imseg.shape[:2]
    nueva = np.zeros([ls, cs, 3], np.uint8)

    #começar a pintura com cores alatórias e para isso eu vou fazer um sorteio entre 0 e 255
    for o in range(os):

        cor = lambda: random.randint(0, 255)

        nueva[np.where(imseg == o + 1)] = [cor(), cor(), cor()]
    
    cv2.imshow('final', nueva)
    cv2.waitKey(0)
