#Abrir uma sequência de imagens coloridas, transformar para tom de cinza cada imagem e obtenha as Texturas de Haralick que são calculadas à partir da matriz de co-ocorrência (GLCM em inglês) de todas estas imagens. Imprima os resultados de cada imagem em um arquivo e na tela do prompt de comandos. Cada linha do arquivo gerado deve representar os atributos obtidos em uma imagem.

import cv2
from skimage import feature
import csv
import glob
import os


def extract_GLCM(imagens, distancias, angulos):
    print('[INFO] Extracting GLCM.')
    GLCM_features = []

    for i, imagem in enumerate(imagens):

        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(imagens)))

        imcolor = cv2.imread(imagem)

        imcolor = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)

        glcm = feature.greycomatrix(imcolor, distancias, angulos, 256, symmetric=False, normed=True)

        glcm_properties = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
        features = [feature.greycoprops(glcm, glcm_property)[0, 0] for glcm_property in glcm_properties]

        GLCM_features.append(features)

    print('\n')

    return GLCM_features

def salvar_resultados(extractor_name, features):


    for vector in features:
        print(vector)

    with open(extractor_name + '.csv', 'w') as outfile:

        writer = csv.writer(outfile)
        writer.writerows(features)


if __name__ == '__main__':

    pasta = 'seq_img'

    imcolor_paths = glob.glob(os.path.join(pasta, '*.jpg'))

    features = extract_GLCM(imcolor_paths, distancias=[5], angulos=[0])

    salvar_resultados('GLCM', features)