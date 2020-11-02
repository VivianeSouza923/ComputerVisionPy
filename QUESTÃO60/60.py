#Calcule a acurácia, a especificidade e a sensibilidade a partir de cada matriz de confusão obtida na questão 59.

import cv2
import csv
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#Obtenha os nomes dos arquivos em uma lista
files = ['true_and_predict_' + str(num) + '.csv' for num in range(53, 59)]

#percorrer os arquivos
for file in files:
    print(file, '\n\n')
    with open(file, 'r') as infile:
        #ler o arquivo csv
        read = csv.reader(infile, delimiter=',')

        #Obtenha os dados dos arquivos lidos
        data = []
        for row in read:
            data.append(row)

        #Crie uma lista para rótulos verdadeiros e preditivos
        true = [int(x) for x in data[0]]
        pred = [int(x) for x in data[1]]

        #Obtenha a matriz de confusão
        cm = confusion_matrix(true, pred)

        #calcular a precisão
        print('Accuracy: {}'.format(accuracy_score(true, pred)))

        #Mostra o relatório de classificação (precisão, recuperação, pontuação f1)
        print('Classification report: \n', classification_report(true, pred))

        print('\n\n###############################################')