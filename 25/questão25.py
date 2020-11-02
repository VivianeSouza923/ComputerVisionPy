#Abrir uma imagem colorida, transformar para tom de cinza e aplique a técnica Crescimento de Regiões (Region Growing). Para isto, faça no paint uma imagem 640×480 com alguns objetos em preto e o fundo seja branco. Neste tópico irão existir mais de um objeto para segmentar, então existe mais de uma região. Inicialize a semente com um clique em cada objeto, em que o primeiro clique rotule o objeto como região 1, pintando a região encontrada de vermelho. Ao terminar de delimitar a região 2, clique em outro objeto, rotulando esta região como 2 e pinte esta região de azul. Faça o mesmo para um terceiro objeto, pintando o mesmo de verde e rotulando sua região como 3. Obs: Ressalto que as regiões que não fazem parte de nenhum objeto devem possuir valor 0.

import cv2
import numpy as np


#abrir uma imagem colorida
imcolor = cv2.imread('image.jpg')

#transformar para tom de cinza
imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

#CRIAR A MATRIZ QUE CONTÉM A REGIÃO SEGMENTADA
matrizzero = np.zeros_like(imcinza)

s = (0, 0) #declarei a semente
ec = 0 #contador de eventos

def CR(imcolor, imcolor_marked, s=None):

    #pegar a forma da imagem/matriz
    ls, cs = imcolor.shape[:2]

    #inicializa as variáveis de comparação e incrementação
    cf = 0
    pp = 1

    #Inicialize a semente em cada objeto
    while pp != cf:
        pp = cf
        cf = 0

        for l in range(ls):
            for c in range(cs):
                if imcolor_marked[l, c] == 1:
                    if imcolor[l-1, c-1] < 230:
                        imcolor_marked[l-1, c-1] = 1
                        cf+=1
                    if imcolor[l-1, c] < 230:
                        imcolor_marked[l-1, c] = 1
                        cf+=1
                    if imcolor[l-1, c+1] < 230:
                        imcolor_marked[l-1, c+1] = 1
                        cf+=1
                    if imcolor[l, c-1] < 230:
                        imcolor_marked[l, c-1] = 1
                        cf+=1
                    if imcolor[l, c+1] < 230:
                        imcolor_marked[l, c+1] = 1
                        cf+=1
                    if imcolor[l+1, c-1] < 230:
                        imcolor_marked[l+1, c-1] = 1
                        cf+=1
                    if imcolor[l+1, c] < 230:
                        imcolor_marked[l+1, c] = 1
                        cf+=1
                    if imcolor[l+1, c+1] < 230:
                        imcolor[l+1, c+1] = 1
                        cf+=1
                
                if imcolor_marked[l, c] == 2:
                    if imcolor[l-1, c-1] < 230:
                        imcolor_marked[l-1, c-1] = 2
                        cf+=1
                    if imcolor[l-1, c] < 230:
                        imcolor_marked[l-1, c] = 2
                        cf+=1
                    if imcolor[l-1, c+1] < 230:
                        imcolor_marked[l-1, c+1] = 2
                        cf+=1
                    if imcolor[l, c-1] < 230:
                        imcolor_marked[l, c-1] = 2
                        cf+=1
                    if imcolor[l, c+1] < 230:
                        imcolor_marked[l, c+1] = 2
                        cf+=1
                    if imcolor[l+1, c-1] < 230:
                        imcolor_marked[l+1, c-1] = 2
                        cf+=1
                    if imcolor[l+1, c] < 230:
                        imcolor_marked[l+1, c] = 2
                        cf+=1
                    if imcolor[l+1, c+1] < 230:
                        imcolor_marked[l+1, c+1] = 2
                        cf+=1
                
                if imcolor_marked[l, c] == 3:
                    if imcolor[l-1, c-1] < 230:
                        imcolor_marked[l-1, c-1] = 3
                        cf+=1
                    if imcolor[l-1, c] < 230:
                        imcolor_marked[l-1, c] = 3
                        cf+=1
                    if imcolor[l-1, c+1] < 230:
                        imcolor_marked[l-1, c+1] = 3
                        cf+=1
                    if imcolor[l, c-1] < 230:
                        imcolor_marked[l, c-1] = 3
                        cf+=1
                    if imcolor[l, c+1] < 230:
                        imcolor_marked[l, c+1] = 3
                        cf+=1
                    if imcolor[l+1, c-1] < 230:
                        imcolor_marked[l+1, c-1] = 3
                        cf+=1
                    if imcolor[l+1, c] < 230:
                        imcolor_marked[l+1, c] = 3
                        cf+=1
                    if imcolor[l+1, c+1] < 230:
                        imcolor_marked[l+1, c+1] = 3
                        cf+=1
                    
    return imcolor_marked

def clique(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global s
        global ec
        global matrizzero

        ec+=1

        matrizzero[y, x] = ec

#exibições
if __name__ == '__main__':
    cv2.namedWindow('Mark Object 1', 1)
    cv2.imshow('Mark Object 1', imcinza)
    cv2.setMouseCallback('Mark Object 1', clique)
    cv2.waitKey(0)

    imseg = CR(imcinza, matrizzero)


    ls, cs = imseg.shape[:2]
    final = np.zeros([ls, cs, 3], np.uint8)

    final[np.where(imseg == 1)] = [255, 0, 0]
    final[np.where(imseg == 2)] = [0, 0, 255]
    final[np.where(imseg == 3)] = [0, 255, 0]

    cv2.imshow('final', final)
    cv2.waitKey(0)

