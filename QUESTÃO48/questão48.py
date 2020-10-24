#Abrir uma sequência de imagens coloridas, transformar para tom de cinza cada imagem e obtenha os momentos de HU (também conhecidos como momentos invariantes) de todas estas imagens. Imprima os resultados de cada imagem em um arquivo e na tela do prompt de comandos. Cada linha do arquivo gerado deve representar os atributos obtidos em uma imagem.

import cv2
import csv
import os
import glob

def extrair_momentos_hu(imagens):

    print('[INFO] Extracting hu moments.')
    momentos_hu_completos = []

    for i, imagem in enumerate(imagens):

        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(imagens)))

        imcolor = cv2.imread(imagem)

        imcolor = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

        momentos = cv2.moments(imcolor)

        momentos_hu = cv2.HuMoments(momentos)
        momentos_novos = [momento[0] for momento in momentos_hu]

        momentos_hu_completos.append(momentos_novos)

    print('\n')
    return momentos_hu_completos



def salvar_resultado(extractor_name, features):

    for vector in features:
        print(vector)

    with open(extractor_name + '.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(features)

if __name__ == '__main__':

    pasta = 'seq_img/'

    caminho = glob.glob(os.path.join(pasta, '*.jpg'))

    features = extrair_momentos_hu(caminho)

    salvar_resultado('momentos_hu', features)