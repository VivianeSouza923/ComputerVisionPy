#Usar o método de classificação Multi Layer Perceptron (MLP) usando a biblioteca de Machine Learning da OpenCv. Deve-se fazer com os métodos Hold Out e Leave One Out. Tudo deve ser feito utilizando a estrutura Mat da OpenCv. Faça os testes com no mínimo três topologias distintas da Rede Neural usada.

import cv2
import pandas as pd
from sklearn.neural_network import MLPClassifier
import csv

#começar criando a função Hold Out. Ela vai receber como parametros: dataframe(df), o tamanho do treino(train_size) e o embaralhar(shuffle) que vai ser True ou False
def hold_out(df, train_size, shuffle=True):
    
    #se shuffle foi 1:
    if shuffle:
        #embaralhe o df. A maneira idiomática de fazer isso com o Pandas é usar o método dataframe para amostrar todas as linhas sem substituição: df.sample(frac=1). O argumento da palavra-chave frac especifica a fração de linhas a retornar na amostra aleatória, então frac = 1 significa retornar todas as linhas (em ordem aleatória). Se desejar embaralhar seu dataframe no local e redefinir o índice, você pode fazer, por exemplo, df = df.sample(frac=1).reset_index(drop=True). Aqui, especificar drop = True evita que .reset_index crie uma coluna contendo as entradas de índice antigas.
        df = df.sample(frac=1).reset_index(drop=True)

    #após embaralhar, eu converto as linhas do dataframe em uma lista de listas e inicio tudo isso criando a data 
    data = []

    #para cada linha dentro das linhas do dataframe:
    for row in df.iterrows():

        #vou dizer que values e index recebem essa linha e vou adicionar à lista data os valores de values transformados em lista.
        index, values = row
        data.append(values.tolist())

    #agora vou dividir a data em treino e teste
    X_train = data[:int(train_size*len(data))]
    X_test = data[int(train_size*len(data)):]

    #Obtenha os rótulos correspondentes para cada vetor de característica
    y_train = [int(x[-1]) for x in X_train]
    y_test = [int(x[-1]) for x in X_test]

    #Remova os rótulos do treino e dos vetores de teste
    X_train = [x[:-1] for x in X_train]
    X_test = [x[:-1] for x in X_test]

    return X_train, X_test, y_train, y_test


def leave_one_out(df, shuffle=True):

    # Shuffle the dataframe if the shuffle is set to true
    if shuffle:
        df = df.sample(frac=1).reset_index(drop=True)

    # Convert the rows of the dataframe into a list of lists
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    #Crie uma lista de listas, na qual cada iteração de deixar um de fora será armazenada
    X_train = []
    X_test = []
    y_train = []
    y_test = []

    #ao percorrer toda a data
    for i in range(len(data)):

        #eu a copio e atribuo a train
        train = data.copy()

        #após isto eu removo a data da vez de train
        train.remove(data[i])

        #o test vai receber a data da vez
        test = data[i]

        #Obtenha os rótulos correspondentes para cada vetor de característica
        y_train.append([int(x[-1]) for x in train])
        y_test.append(int(test[-1]))

        #Remova os rótulos do treino e dos vetores de teste
        X_train.append([x[:-1] for x in train])
        X_test.append(test[:-1])

    return X_train, X_test, y_train, y_test

#criar a função ler dados (read_data) que irá receber como parametro file.
def read_data(file):
    #Carregar os recursos de um arquivo em um dataframe
    return pd.read_csv(file, sep=',', header=None)


if __name__ == '__main__':

    ##Leia o arquivo com os recursos para classificar
    filename = 'features.txt'
    features = read_data(filename)

    #divida a database utilizando hold out 
    X_train, X_test, y_train, y_test = hold_out(features, train_size=0.9)

    #Crie um objeto mlp (altere os parâmetros hidden_layer para alterar a topologia do modelo)
    mlp = MLPClassifier(hidden_layer_sizes=(5, 3), max_iter=3000)

    #treine o modelo
    mlp.fit(X_train, y_train)

    #Avalie nos dados de teste
    predictions = mlp.predict(X_test)

    #Converta os resultados em uma lista
    predictions = list(predictions)

    #calcular a precisão usando hold out
    count = 0
    for x, y in zip(y_test, predictions):
        if x == y:
            count += 1

    accuracy = count/len(y_test)
    print('Accuracy using hold out: {:.4f}'.format(accuracy))

    #salvar os rótulos verdadeiros e previstos
    with open('true_and_predict_56.csv', 'w') as outfile:
        rows = [y_test, predictions]
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(rows)

    #separar a database usando leave one out 
    X_train, X_test, y_train, y_test = leave_one_out(features)

    #aplicar o mlp
    print('[INFO] Starting leave one out training...')
    count = 0
    sample_count = 0
    for train_set, test_set, label_train, label_test in zip(X_train, X_test, y_train, y_test):
        print('[INFO] Training sample {}/{}'.format(sample_count+1, len(y_train)))
        sample_count += 1

        #Crie um objeto mlp (altere os parâmetros hidden_layer para alterar a topologia do modelo)
        mlp = MLPClassifier(hidden_layer_sizes=(5, 3), max_iter=3000)

        #treine o modelo
        mlp.fit(train_set, label_train)

        #Avalie nos dados de teste
        new_list = []
        new_list.append(test_set)
        prediction = mlp.predict(new_list)

        if prediction == label_test:
            count += 1

    accuracy = count / len(y_test)
    print('Accuracy using leave one out: {:.4f}'.format(accuracy))

