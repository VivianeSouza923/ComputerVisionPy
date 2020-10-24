#Implementar o método de classificação k-médias (K-means em inglês) usando os métodos Hold out e Leave One Out. Tudo deve ser feito utilizando a estrutura Mat da OpenCv. Deve ser implementado o KNN com o K igual a 1, 3 e 7. Obs: Não usar as classes de Machine Learning da OpenCv.

import pandas as pd
import math
import numpy as np
import csv

#começar criando a função Hold Out. Ela vai receber como parametros: dataframe(df), o tamanho do treino(train_size) e o embaralhar(shuffle) que vai ser True ou False
def hold_out(df, train_size, shuffle=True):
    
    # Embaralhe o dataframe se o shuffle(do inglÊs, embaralhar) estiver definido como verdadeiro
    #se o shuffle existir, ou seja, for verdadeiro:
    if shuffle:
        #embaralhar o dataframe. A maneira idiomática de fazer isso com o Pandas é usar o método dataframe para amostrar todas as linhas sem substituição: df.sample(frac=1). O argumento da palavra-chave frac especifica a fração de linhas a retornar na amostra aleatória, então frac = 1 significa retornar todas as linhas (em ordem aleatória). Se desejar embaralhar seu dataframe no local e redefinir o índice, você pode fazer, por exemplo, df = df.sample(frac=1).reset_index(drop=True). Aqui, especificar drop = True evita que .reset_index crie uma coluna contendo as entradas de índice antigas.
        df = df.sample(frac=1).reset_index(drop=True)

    #converter as linhas do dataframe em uma lista de listas
    #crio a matriz chamada data
    data = []
    #para cada linha nas linhas do dataframe
    for row in df.iterrows():
        #eu vou dizer que index e values são iguais a linha
        index, values = row
        data.append(values.tolist())

     #divida os dados em treinar e testar
    X_train = data[:int(train_size*len(data))]
    X_test = data[int(train_size*len(data)):]

    #Obtenha os rótulos correspondentes para cada vetor de característica
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

#Implementar o método de classificação k-médias (K-means em inglês)
class KMeans:

    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.centroids = {}

    def fit(self, data):
        #Inicialize os centróides, os primeiros elementos 'k' no conjunto de dados serão nossos centróides iniciais
        for i in range(self.k):
            self.centroids[i] = data[i]

        #Comece as iterações
        for i in range(self.max_iterations):
            self.classes = {}
            for i in range(self.k):
                self.classes[i] = []

            ##Encontre a distância entre o ponto e o cluster; escolha o centróide mais próximo
            for features in data:
                distances = [np.linalg.norm(np.array(features) - np.array(self.centroids[centroid])) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classes[classification].append(features)

            previous = dict(self.centroids)

            ##Faça a média dos pontos de dados do cluster para recalcular os centróides. #np.average pode calcular uma média ponderada se o weightsparâmetro for fornecido. Axis = Eixo ou eixos ao longo do qual calcular a média a. O padrão, axis = None, fará a média de todos os elementos da matriz de entrada. Se o eixo for negativo, ele conta do último ao primeiro eixo.
            for classification in self.classes:
                self.centroids[classification] = np.average(self.classes[classification], axis=0)

            isOptimal = True

            for centroid in self.centroids:
                original_centroid = previous[centroid]

                current = self.centroids[centroid]

                #Soma dos elementos da matriz em um determinado eixo.
                if np.sum((current - original_centroid)/original_centroid * 100) > self.tolerance:
                    isOptimal = False

            #sair do loop principal se os resultados forem ótimos, ou seja, os centróides não mudam suas posições muito (mais do que a nossa tolerância)
            if isOptimal:
                break


    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification


if __name__ == '__main__':

    ##Leia o arquivo com os recursos para classificar
    filename = 'features.txt'
    features = read_data(filename)

    #divida a database usando HOld Out
    X_train, X_test, y_train, y_test = hold_out(features, train_size=0.9)

    ## Aplicar k-means (você pode alterar o número de clusters que deseja encontrar, obs .: Se você colocar um número de cluster
    # maior do que o número de classes, o algoritmo retornará previsões de classes que não existem no base de dados.)
    km = KMeans(k=3, max_iterations=10000)
    km.fit(X_train)

    predictions = []
    for test in X_test:
        predictions.append(km.predict(test))

    #Calcula a precisão usando usando Hold OUt
    count = 0
    for x, y in zip(y_test, predictions):
        if x == y:
            count += 1

    accuracy = count/len(y_test)
    print('Accuracy using hold out: {:.4f}'.format(accuracy))

    # #Salve os rótulos verdadeiros e previstos
    with open('true_and_predict_54.csv', 'w') as outfile:
        rows = [y_test, predictions]
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(rows)

    # If you want to plot yours clusters, uncomment the following lines
    # # Plotting starts here
    # colors = 10 * ["r", "g", "c", "b", "k"]
    #
    # for centroid in km.centroids:
    #     plt.scatter(km.centroids[centroid][0], km.centroids[centroid][1], s=130, marker="x")
    #
    # for classification in km.classes:
    #     color = colors[classification]
    #     for feature in km.classes[classification]:
    #         plt.scatter(feature[0], feature[1], color=color, s=30)
    #
    # plt.show()

    # #divida a database usando leave one out
    X_train, X_test, y_train, y_test = leave_one_out(features)

    # A#aplique knn

    count = 0
    for train_set, test_set, label_train, label_test in zip(X_train, X_test, y_train, y_test):

         #aplicar k-means (você pode alterar o número de clusters que deseja encontrar, obs .: se você colocar um número de clusters
        # maior do que o número de classes, o algoritmo retornará previsões de classes que não existem no
        # base de dados.)
        km = KMeans(k=3, max_iterations=10000)
        km.fit(train_set)

        predictions = []

        predict = km.predict(test_set)

        if predict == label_test:
            count += 1

    accuracy = count / len(y_test)
    print('Accuracy using leave one out: {:.4f}'.format(accuracy))