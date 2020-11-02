#Faça o mesmo que a questão 26, entretanto gere subimagens com os objetos detectados e apresente estas subimagens, uma em cada janela.

import cv2
import random
import numpy as np

def CR(imcolor):

    ls, cs = imcolor.shape[:2]

    matrizzero = np.zeros_like(imcolor)

    object_found = 0

    for ext_l in range(ls):
        for ext_c in range(cs):
            if matrizzero[ext_l, ext_c] == 0 and imcolor[ext_l, ext_c] < 230:
                object_found+=1
                matrizzero[ext_l, ext_c] = object_found

                cf = 0
                pp = 1

                while pp != cf:
                    pp = cf
                    cf = 0

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

if __name__ == '__main__':

    imcolor = cv2.imread('image.jpg')

    imcinza = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imcinza', imcinza)
    cv2.waitKey(0)


    imseg, os = CR(imcinza)

    ls, cs = imseg.shape[:2]    
    nueva = np.zeros([ls, cs, 3], np.uint8)

    for o in range(os):

        cor = lambda: random.randint(0, 255)


        x_min = 0
        x_max = 0
        y_min = 0
        y_max = 0

        for l in range(ls):
            for c in range(cs):
                if imseg[l, c] == o + 1:
                    if x_min > c:
                        x_min = c
                    if x_max < c:
                        x_max = c
                    if y_min > l:
                        y_min = l
                    if y_max < l:
                        y_max = l
                    
                    if x_min == 0:
                        x_min = x_max
                    if y_min == 0:
                        y_min = y_max

        
        nueva[np.where(imseg == o + 1)] = [cor(), cor(), cor()]


        ob = nueva[y_min:y_max, x_min:x_max]

        cv2.imshow('final '+ str(o), ob)
        cv2.waitKey(10)
    cv2.waitKey(0)


