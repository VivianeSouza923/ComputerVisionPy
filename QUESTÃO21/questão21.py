#Faça o mesmo que o tópico 21, alterando apenas o modo de inicializar a semente, onde esta deve ser inicializada com um click na imagem apresentada pela OpenCv.

import cv2
import numpy as np

s = (0,0)



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


#o clique
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global s


        s = (x, y)


if __name__ == '__main__':

    #abrir uma imagem colorida
    imcolor = cv2.imread('e.jpg')

    #transformar para tom de cinza
    imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('Original Image', 1)
    cv2.imshow('Original image', imcinza)
    cv2.setMouseCallback('Original image', mouse_event)
    cv2.waitKey(0)

    imseg = CR(imcinza, s)

    cv2.imshow('final', imseg)
    cv2.waitKey(0)
    
    

