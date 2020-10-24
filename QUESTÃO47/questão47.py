#Abrir uma sequência de imagens coloridas, transformar para tom de cinza cada imagem e obtenha os momentos centrais de todas estas imagens. Imprima os resultados de cada imagem em um arquivo e na tela do prompt de comandos. Cada linha do arquivo gerado deve representar os atributos obtidos em uma imagem.

import cv2
import csv
import os
import glob

def extrair_momentos_centrais(imagens):

    print('[INFO] Extracting central moments.')
    momentos_centrais = []

    for i, imagem in enumerate(imagens):

        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(imagens)))

        imcolor = cv2.imread(imagem)

        imcolor = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

        momentos = cv2.moments(imcolor)

        momentos_centrais.append([momentos['mu20'], momentos['mu11'], momentos['mu02'], momentos['mu30'], momentos['mu21'], momentos['mu12'], momentos['mu03']])

    print('\n')

    return momentos_centrais

def salvar_resultado(extractor_name, features):

    for vector in features:
        print(vector)

    with open(extractor_name + '.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(features)

if __name__ == '__main__':

    pasta = 'seq_img/'

    caminho = glob.glob(os.path.join(pasta, '*.jpg'))

    features = extrair_momentos_centrais(caminho)

    salvar_resultado('momentos_centrais', features)

