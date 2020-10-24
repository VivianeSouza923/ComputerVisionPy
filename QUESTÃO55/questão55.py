#Usar o método de classificação pelo vizinho mais próximo (KNN em inglês) usando a biblioteca de Machine Learning da OpenCv. Deve-se fazer com os métodos Hold Out e Leave One Out. Tudo deve ser feito utilizando a estrutura Mat da OpenCv.

import cv2
import pandas as pd
import math
import numpy as np
import operator
import csv

#começar criando a função Hold Out. Ela vai receber como parametros: dataframe(df), o tamanho do treino(train_size) e o embaralhar(shuffle) que vai ser True ou False
def hold_out(df, train_size, shuffle=True):
    
    #Embaralhe o dataframe se o shuffle(do inglÊs, embaralhar) estiver definido como verdadeiro
    #se o shuffle existir, ou seja, for verdadeiro:
    if shuffle:
        #embaralhar o dataframe. A maneira idiomática de fazer isso com o Pandas é usar o método dataframe para amostrar todas as linhas sem substituição: df.sample(frac=1). O argumento da palavra-chave frac especifica a fração de linhas a retornar na amostra aleatória, então frac = 1 significa retornar todas as linhas (em ordem aleatória). Se desejar embaralhar seu dataframe no local e redefinir o índice, você pode fazer, por exemplo, df = df.sample(frac=1).reset_index(drop=True). Aqui, especificar drop = True evita que .reset_index crie uma coluna contendo as entradas de índice antigas.
        df = df.sample(frac=1).reset_index(drop=True)

    #converter as linhas do dataframe em uma lista de listas
    #crio a matriz chamada data
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    #divida os dados em treino e teste
    X_train = data[:int(train_size*len(data))]
    X_test = data[int(train_size*len(data)):]

   ##Obtenha os rótulos correspondentes para cada vetor de característica
    y_train = [int(x[-1]) for x in X_train]
    y_test = [int(x[-1]) for x in X_test]

    ##Remova os rótulos do treino e dos vetores de teste
    X_train = [x[:-1] for x in X_train]
    X_test = [x[:-1] for x in X_test]

    #retornar resultados
    return X_train, X_test, y_train, y_test

#criar a função leave one out que irá receber como parametros o dataframe e o shuffle(vou embaralhar ou não?
def leave_one_out(df, shuffle=True):

    # Embaralhe o dataframe se o shuffle estiver definido como verdadeiro
    if shuffle:
        df = df.sample(frac=1).reset_index(drop=True)

    #converter as linhas do dataframe em uma lista de listas
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    #Crie uma lista de listas, na qual cada iteração de deixar um de fora será armazenada
    X_train = []
    X_test = []
    y_train = []
    y_test = []

    #na qual cada iteração de deixar um de fora
    for i in range(len(data)):
        train = data.copy()
        train.remove(data[i])

        #será armazenada
        test = data[i]

        ###Obtenha os rótulos correspondentes para cada vetor de característica
        y_train.append([int(x[-1]) for x in train])
        y_test.append(int(test[-1]))

        ##Remova os rótulos do trem e dos vetores de teste
        X_train.append([x[:-1] for x in train])
        X_test.append(test[:-1])

    return X_train, X_test, y_train, y_test

##criar a função ler dados (read_data) que irá receber como parametro file.
def read_data(file):
    # Load the features of a file in a dataframe
    return pd.read_csv(file, sep=',', header=None)

##criar a função euclidean_dist (distância entre doispontos. raiz(x-y)²) que receberá como parametro x1, x2. 
def euclidean_dist(x1, x2):
    dist = 0.0
    for x, y in zip(x1, x2):
        dist += pow(float(x) - float(y), 2)
    dist = math.sqrt(dist)

    return dist

##criar a função knn que recebrá como parametros os x train e test, y_train e k_neighbors=3(vizinhos = 3)
def knn_clf(X_train, X_test, y_train, k_neighbors=3):
    assert (k_neighbors % 2), 'Number of neighbors must be odd!'

    ##O assert é uma verificação em tempo de execução de uma condição qualquer. Se a condição não for verdadeira, uma exceção AssertionError acontece e o programa pára.
    assert (k_neighbors % 2), 'O número de vizinhos deve ser par!'
    predict = []
    for x1 in X_test:
        class_prediction = np.zeros(max(y_train) + 1)
        euclidean_distance = []

        for x2, label2 in zip(X_train, y_train):
            eu_dist = euclidean_dist(x1, x2)
            euclidean_distance.append((label2, eu_dist))
            euclidean_distance.sort(key=operator.itemgetter(1))
            smaller_k_distances = euclidean_distance[:k_neighbors]

            for label, dist in smaller_k_distances:
                class_prediction[int(label)] += 1

        predict.append(max(range(len(class_prediction)), key=class_prediction.__getitem__))

    return predict


if __name__ == '__main__':

    ##Leia o arquivo com os recursos para classificar
    filename = 'features.txt'
    features = read_data(filename)

    #divida a database usando HOld Out
    X_train, X_test, y_train, y_test = hold_out(features, train_size=0.9)

    #remodelar os dados da etiqueta do trem para se ajustar ao formato do opencv
    y_train = np.reshape(y_train, (-1, 1))

    ##aplique o knn
    knn = cv2.ml.KNearest_create()
    knn.train(np.asarray(X_train, np.float32), cv2.ml.ROW_SAMPLE, y_train)

    #fazer a previsão nos dados de teste!!
    ret, results, neighbors, dist = knn.findNearest(np.asarray(X_test, np.float32), k=3)

    ##converter os resultados em lista 
    predictions = [int(x) for x in results]

    #calcular a precisão usando o método hold out
    count = 0
    for x, y in zip(y_test, predictions):
        if x == y:
            count += 1

    accuracy = count/len(y_test)
    print('Accuracy using hold out: {:.4f}'.format(accuracy))

    ##Salve os rótulos verdadeiros e previstos
    with open('true_and_predict_55.csv', 'w') as outfile:
        rows = [y_test, predictions]
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(rows)

    #dividir a database usando leave one out
    X_train, X_test, y_train, y_test = leave_one_out(features)

    ##aplicar knn
    predictions = np.zeros(int(max(y_train[0])) + 1)
    count = 0
    for train_set, test_set, label_train, label_test in zip(X_train, X_test, y_train, y_test):

        #remodelar os dados da etiqueta do trem para se ajustar ao formato do opencv
        label_train = np.reshape(label_train, (-1, 1))

        knn = cv2.ml.KNearest_create()
        knn.train(np.asarray(train_set, np.float32), cv2.ml.ROW_SAMPLE, label_train)

        #Prever nos dados de teste (você pode variar o número de k)
        test_list = []
        test_list.append(test_set)
        ret, results, neighbors, dist = knn.findNearest(np.asarray(test_list, np.float32), k=3)

        if results[0] == label_test:
            count += 1

    accuracy = count / len(y_test)

    print('Accuracy using leave one out: {:.4f}'.format(accuracy))