#Usar o método de classificação de Bayes usando a biblioteca de Machine Learning da OpenCv. Deve-se fazer com os métodos Hold Out e Leave One Out. Tudo deve ser feito utilizando a estrutura Mat da OpenCv.

import cv2
import pandas as pd
import csv
from sklearn.naive_bayes import GaussianNB

#começo criando a função hold out que receberá como parametros o dataframe(df), o tamanho do treino(o train_size) e o shuffle que é quem vai nos dizer se haverá embaralhamento do dataframe ou não
def hold_out(df, train_size, shuffle=True):
    
    #se o embaralhamento existir:
    if shuffle:
        #O faça. A maneira idiomática de fazer isso com o Pandas é usar o método dataframe para amostrar todas as linhas sem substituição: df.sample(frac=1). O argumento da palavra-chave frac especifica a fração de linhas a retornar na amostra aleatória, então frac = 1 significa retornar todas as linhas (em ordem aleatória). Se desejar embaralhar seu dataframe no local e redefinir o índice, você pode fazer, por exemplo, df = df.sample(frac=1).reset_index(drop=True). Aqui, especificar drop = True evita que .reset_index crie uma coluna contendo as entradas de índice antigas.
        df = df.sample(frac=1).reset_index(drop=True)

    #agora eu vou começar a transformar as linhas do dataframe em uma lista de lis
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    #após isso, dividir os dados em treino e teste
    X_train = data[:int(train_size*len(data))]
    X_test = data[int(train_size*len(data)):]

    #pegar os rótulos correspondentes para cada vetor de característica
    y_train = [int(x[-1]) for x in X_train]
    y_test = [int(x[-1]) for x in X_test]

    #remover os rótulos dos vetores de teste e treino
    X_train = [x[:-1] for x in X_train]
    X_test = [x[:-1] for x in X_test]

    return X_train, X_test, y_train, y_test

#criar a função leave one out que receberá como parametros o dataframe(df) e o shuflle=TRrue que é o que vai ossibilitar o embaralhamento do dataframe
def leave_one_out(df, shuffle=True):

    #se shuffle for 1:
    if shuffle:
        #vamos fazer o embaralhamento
        df = df.sample(frac=1).reset_index(drop=True)

    #converter as linhas do dataframe em uma lista de listas
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    # Create a list of lists, in which each iteration of leave one out will be stored
    X_train = []
    X_test = []
    y_train = []
    y_test = []

    for i in range(len(data)):
        train = data.copy()
        train.remove(data[i])

        test = data[i]

        #pegar os rótulos correspondentes para cada vetor de característica 
        y_train.append([int(x[-1]) for x in train])
        y_test.append(int(test[-1]))

         #remover os rótulos dos vetores de treino e teste
        X_train.append([x[:-1] for x in train])
        X_test.append(test[:-1])

    return X_train, X_test, y_train, y_test

#criar a função read_data quevai receber como paraetro o file.
def read_data(file):
    # Load the features of a file in a dataframe
    return pd.read_csv(file, sep=',', header=None)


if __name__ == '__main__':

    # Read the file with the features to classify
    filename = 'features.txt'
    features = read_data(filename)

    #divida a database usando hold out
    X_train, X_test, y_train, y_test = hold_out(features, train_size=0.9)

     #criar um objeto naive-bayes
    bayes = GaussianNB()

    #treine o model 
    bayes.fit(X_train, y_train)

    #Avalie nos dados de teste
    predictions = bayes.predict(X_test)

    #converter os resultados em uma lista
    predictions = list(predictions)

    #calcular a precisão usando hold out
    count = 0
    for x, y in zip(y_test, predictions):
        if x == y:
            count += 1

    accuracy = count/len(y_test)
    print('Accuracy using hold out: {:.4f}'.format(accuracy))

    #salve os rótulos verdadeiros e previstos
    with open('true_and_predict_58.csv', 'w') as outfile:
        rows = [y_test, predictions]
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(rows)

    #dividir a databse usando leave one out
    X_train, X_test, y_train, y_test = leave_one_out(features)

    #aplicar o bayes
    print('[INFO] Starting leave one out training...')
    count = 0
    sample_count = 0
    for train_set, test_set, label_train, label_test in zip(X_train, X_test, y_train, y_test):
        print('[INFO] Training sample {}/{}'.format(sample_count+1, len(y_train)))
        sample_count += 1

        #criar um objeto naive-bayes
        bayes = GaussianNB()

        #treinar o modelo
        bayes.fit(train_set, label_train)

        #Avalie nos dados de teste
        new_list = []
        new_list.append(test_set)
        prediction = bayes.predict(new_list)

        if prediction == label_test:
            count += 1

    accuracy = count / len(y_test)

    print('Accuracy using leave one out: {:.4f}'.format(accuracy))