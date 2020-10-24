#Abrir uma sequência de imagens coloridas, transformar para tom de cinza cada imagem e obtenha os Local Binary Pattern (LBP) de todas estas imagens. Imprima os resultados de cada imagem em um arquivo e na tela do prompt de comandos. Cada linha do arquivo gerado deve representar os atributos obtidos em uma imagem.

import cv2
from skimage import feature
import numpy as np
import csv
import glob
import os


#primeiro eu vou criar a função que vai extrair o LBP dde todas as imagens.
def extrair_LBP(imagens, número_pontos, raio, eps=1e-7):
    
    #printar a mensagem que deve aparecer na tela indicando que a extração começou
    print('[INFO] Extracting LBP.')
    
    #criei a variável que vai receber a imagem/matriz
    lbp_features = []

    #para cada i, imagem dentro de imagens eu vou:   
    for i, imagem in enumerate(imagens):

        #eu vou imprimir a mensagem que contém no print
        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(imagens)))

        #abrir uma imagem colorida
        imcolor = cv2.imread(imagem)

        #transformar a imagem para tom de cinza
        imcolor = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

        #extrair o lbp
        lbp = feature.local_binary_pattern(imcolor, número_pontos, raio, method='uniform')

        #calcula o histograma da imagem lbp
        ret, histograma = np.histogram(lbp.ravel(), bins = np.arange(0, número_pontos + 3), range=(0, número_pontos + 2))

        histograma = histograma.astype('float')
        histograma /= (histograma.sum() + eps)

        #criar o vetor de recurso exraído por lbp
        imcolor_lbp = [item for item in list(histograma)] 

        lbp_features.append(imcolor_lbp)

    print('\n')

    return lbp_features    

def salvar_resultados(extractor_name, features):

    for vector in features:
        print(vector)

    with open(extractor_name + '.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(features)    

if __name__ == '__main__':

    pasta = 'seq_img'

    imcolor_paths = glob.glob(os.path.join(pasta, '*.jpg'))

    features = extrair_LBP(imcolor_paths, número_pontos=24, raio=8)

    salvar_resultados('LBP', features)