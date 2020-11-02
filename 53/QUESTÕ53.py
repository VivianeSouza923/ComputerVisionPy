#Implementar o método de classificação do vizinho mais próximo (KNN em inglês) usando os métodos Hold out e Leave One Out. Tudo deve ser feito utilizando a estrutura Mat da OpenCv. Deve ser implementado o KNN com o K igual a 1, 3 e 7. Obs: Não usar as classes de Machine Learning da OpenCv.

import pandas as pd
import math
import numpy as np
import operator
import csv

#criar a função Hold Out, ela vai receber o dataframe, o tamanho do treino e o embaralhar (vai receber True ou False, vai saber se é pra embaralhar ou não)
def hold_out(df, train_size, shuffle=True):
    
    # Embaralhe o dataframe se o shuffle(do inglÊs, embaralhar) estiver definido como verdadeiro
    #se o shuffle existir, ou seja, for verdadeiro:
    if shuffle:

        #embaralhar o dataframe. A maneira idiomática de fazer isso com o Pandas é usar o método dataframe para amostrar todas as linhas sem substituição: df.sample(frac=1). O argumento da palavra-chave frac especifica a fração de linhas a retornar na amostra aleatória, então frac = 1 significa retornar todas as linhas (em ordem aleatória). Se desejar embaralhar seu dataframe no local e redefinir o índice, você pode fazer, por exemplo, df = df.sample(frac=1).reset_index(drop=True). Aqui, especificar drop = True evita que .reset_index crie uma coluna contendo as entradas de índice antigas.
        df = df.sample(frac=1).reset_index(drop=True)

    #Converter as linhas do dataframe em uma lista de listas.
    #crio a matriz chamada data
    data = []

    #para cada linha nas linhas do dataframe
    for row in df.iterrows():
        #eu vou dizer que o index e values são iguais a linha.
        index, values = row
        data.append(values.tolist())

    #Divida os dados em treinar e testar
    X_train = data[:int(train_size*len(data))]
    X_test = data[int(train_size*len(data)):]

    #Obtenha os rótulos correspondentes para cada vetor de característica
    y_train = [int(x[-1]) for x in X_train]
    y_test = [int(x[-1]) for x in X_test]

    #Remova os rótulos do treino e dos vetores de teste
    X_train = [x[:-1] for x in X_train]
    X_test = [x[:-1] for x in X_test]

    return X_train, X_test, y_train, y_test

#criar a função leave one out que irá receber como parametros o dataframe e o shuffle(vou embaralhar ou não?)
def leave_one_out(df, shuffle=True):

    # Embaralhe o dataframe se o shuffle estiver definido como verdadeiro
    if shuffle:
        df = df.sample(frac=1).reset_index(drop=True)

    #Converta as linhas do dataframe em uma lista de listas
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    #Crie uma lista de listas, na qual cada iteração de deixar um de fora será armazenada
    X_train = []
    X_test = []
    y_train = []
    y_test = []

    for i in range(len(data)):
        train = data.copy()
        train.remove(data[i])

        test = data[i]

        #Obtenha os rótulos correspondentes para cada vetor de característica
        y_train.append([int(x[-1]) for x in train])
        y_test.append(int(test[-1]))

        #Remova os rótulos do trem e dos vetores de teste
        X_train.append([x[:-1] for x in train])
        X_test.append(test[:-1])

    return X_train, X_test, y_train, y_test

#criar a função ler dados (read_data) que irá receber como parametro file.
def read_data(file):
    #Carregar os recursos de um arquivo em um dataframe
    return pd.read_csv(file, sep=',', header=None)

#criar a função euclidean_dist que receberá como parametro x1, x2. 
def euclidean_dist(x1, x2):
    dist = 0.0
    for x, y in zip(x1, x2):
        dist += pow(float(x) - float(y), 2)
    dist = math.sqrt(dist)

    return dist

#criar a função knn que recebrá como parametros os x train e test, y_train e k_neighbors=3(vizinhos = 3)
def knn_clf(X_train, X_test, y_train, k_neighbors=3):
    #O assert é uma verificação em tempo de execução de uma condição qualquer. Se a condição não for verdadeira, uma exceção AssertionError acontece e o programa pára.
    assert (k_neighbors % 2), 'O número de vizinhos deve ser par!'

    #prever
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

    #Leia o arquivo com os recursos para classificar
    filename = 'features.txt'
    features = read_data(filename)

    #Divida A DATABASE usando hold out
    X_train, X_test, y_train, y_test = hold_out(features, train_size=0.8)

    #Aplique knn 
    predictions = knn_clf(X_train, X_test, y_train, k_neighbors=7)

    #Calcula a precisão usando hold out
    count = 0
    for x, y in zip(y_test, predictions):
        if x == y:
            count += 1

    accuracy = count/len(y_test)
    print('Accuracy using hold out: {:.4f}'.format(accuracy))

    #SALVAR OS RÓTULOS VERDADEIROS E PREVISTOS
    with open('true_and_predict_53.csv', 'w') as outfile:
        rows = [y_test, predictions]
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(rows)

    # DIVIDA A DATABASE USANDO leave one out
    X_train, X_test, y_train, y_test = leave_one_out(features)

    # ApLIQUE knn 
    predictions = np.zeros(int(max(y_train[0])) + 1)
    count = 0
    for train_set, test_set, label_train, label_test in zip(X_train, X_test, y_train, y_test):

        test_list = []
        test_list.append(test_set)
        predict = knn_clf(train_set, test_list, label_train, k_neighbors=7)
        predictions[predict] += 1

        if predict[0] == label_test:
            count += 1

    accuracy = count / len(y_test)

    print('Accuracy using leave one out: {:.4f}'.format(accuracy))