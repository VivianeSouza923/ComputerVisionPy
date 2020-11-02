#Abrir uma imagem colorida, transformar para tom de cinza e aplique a técnica Crescimento de Regiões (Region Growing). Para isto, inicialmente faça uma imagem com dimensões 320×240 no paint, onde o fundo da imagem seja branco e exista um círculo preto no centro. Utilize algum ponto dentro do circulo preto como semente, onde você deve determinar este ponto analisando imagem previamente. A regra de adesão do método deve ser: “Sempre que um vizinho da região possuir tom de cinza menor que 127, deve-se agregar este vizinho à região”. Aplique o Crescimento de Regiões de forma iterativa, em que o algoritmo irá estabilizar apenas quando a região parar de crescer.

import cv2
import numpy as np

#abrir uma imagem colorida
imcolor = cv2.imread('e.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#aplique a técninca Crescimento de REgiões(Region Growing)
def CR(imcinza, s=None): #definindo a função... ela vai receber a minha imagem e a chamada semente que vai estar vazia, zerada etc.

    #pega a forma da matriz/imagem pra gente poder utilizar no for
    ls, cs = imcinza.shape[:2]

    #pegar o ponto do nosso s, que é nossa semente. 
    xc, yc = s

    #finalmente eu vou criar a matriz que será analisada dentro do for
    matriz = np.zeros_like(imcinza)

    #próximo passo é marcar o ponto no circulo
    matriz[xc, yc] = 255

    #vou iniciar as variáveis de contagem e comparação que vão fazer parte do crescimento da semente no laço
    cr = 0 
    pp = 1

    #processo de crescimento da semente
    while pp != cr:

        pp = cr
        cr = 0
        for l in range(ls):
            for c in range(cs):
                if matriz[l, c] == 255:
                    if imcinza[l-1, c-1]< 127:
                        matriz[l-1, c-1] = 255
                        cr += 1
                    if imcinza[l-1, c]< 127:
                        matriz[l-1, c] = 255
                        cr += 1
                    if imcinza[l-1, c+1]< 127:
                        matriz[l-1, c+1] = 255
                        cr+=1
                    if imcinza[l, c-1]< 127:
                        matriz[l, c-1] = 255
                        cr+=1
                    if imcinza[l, c]< 127:
                        matriz[l, c] = 255
                        cr+=1
                    if imcinza[l, c+1]< 127:
                        matriz[l, c+1] = 255
                        cr+=1
                    if imcinza[l+1, c-1]< 127:
                        matriz[l+1, c-1] = 255
                        cr+=1
                    if imcinza[l+1, c]< 127:
                        matriz[l+1, c] = 255
                        cr+=1
                    if imcinza[l+1, c+1]< 127:
                        matriz[l+1, c+1] = 255
                        cr+=1

    return matriz


imseg = CR(imcinza, s=(int(imcinza.shape[0]/2), int(imcinza.shape[1]/2)))

cv2.imshow('visualizar', imseg)
cv2.waitKey(0)
                        

