#Usar o método de classificação do SVC (Support Vector Classifier) usando a biblioteca de Machine Learning da OpenCv. Deve-se fazer com os métodos Hold Out e Leave One Out. Tudo deve ser feito utilizando a estrutura Mat da OpenCv. Faça os testes do SVM com os Kernels Linear, polinomial, Sigmoidal e RBF.


import cv2
import pandas as pd
from sklearn.svm import SVC
import csv

#começar criando a função Hold Out. Ela vai receber como parametros: dataframe(df), o tamanho do treino(train_size) e o embaralhar(shuffle) que vai ser True ou False
def hold_out(df, train_size, shuffle=True):

    #casa haja shuffle:
    if shuffle:
        #faça o embaralhamento
        df = df.sample(frac=1).reset_index(drop=True)

    #Converter as linhas do dataframe em uma lista de listas
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    # dividir os dados em treino e test
    X_train = data[:int(train_size*len(data))]
    X_test = data[int(train_size*len(data)):]

    # pegue os rótulos correspondentes para cada vetor de característica
    y_train = [int(x[-1]) for x in X_train]
    y_test = [int(x[-1]) for x in X_test]

    # Remova os rótulos dos vetores de treino e teste
    X_train = [x[:-1] for x in X_train]
    X_test = [x[:-1] for x in X_test]

    #retornar resultados
    return X_train, X_test, y_train, y_test

#criar a função leave one out. Ela receberá  como parametros o df(dataframe) e shuffle=True para que haja o embaralhamento do df
def leave_one_out(df, shuffle=True):

    # se shuffle for igual a true:
    if shuffle:

        #embaralhe o dataframe
        df = df.sample(frac=1).reset_index(drop=True)

    #converter as linhas do dataframe em uma lista de listas
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    # Crie uma lista de listas, na qual cada iteração de deixar um de fora será armazenada
    X_train = []
    X_test = []
    y_train = []
    y_test = []

    #vou percorrer toda a minha len(data) e o meu trai vai receber a cópia de data, após isso será removido de train a data da vez
    for i in range(len(data)):
        train = data.copy()
        train.remove(data[i])

        #test vai receber a data da vez
        test = data[i]

        # pegue os rótulos correspondentes para cada vetor de característica
        y_train.append([int(x[-1]) for x in train])
        y_test.append(int(test[-1]))

        # remova os rótulos dos vetores de teste e treino
        X_train.append([x[:-1] for x in train])
        X_test.append(test[:-1])

    #finalmente, retorno os resultados!
    return X_train, X_test, y_train, y_test

#vou criar a função read_data qeu irá receber como parametro o file
def read_data(file):

    # Carregar os recursos de um arquivo em um dataframe
    return pd.read_csv(file, sep=',', header=None)


if __name__ == '__main__':

    # Leia o arquivo com os recursos para classificar
    filename = 'features.txt'
    features = read_data(filename)

    # divida a database utilizando o hold out
    X_train, X_test, y_train, y_test = hold_out(features, train_size=0.9)

    # criar um objeto SVC (aqui eu posso ficar mudando o kernel. posso utilizar o rbf, poly, linear, sigmoid)
    svc = SVC(kernel='rbf', gamma='auto')

    # Treine o model
    svc.fit(X_train, y_train)

    # Avalie nos dados de teste
    predictions = svc.predict(X_test)

    # Converter os resultados em uma lista
    predictions = list(predictions)

    # calcular a precisão utilizando hold out
    count = 0
    for x, y in zip(y_test, predictions):
        if x == y:
            count += 1

    accuracy = count/len(y_test)
    print('Accuracy using hold out: {:.4f}'.format(accuracy))

    # Salve os rótulos verdadeiros e previstos
    with open('true_and_predict_57.csv', 'w') as outfile:
        rows = [y_test, predictions]
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(rows)

    #divida a database utilizando o leave one out
    X_train, X_test, y_train, y_test = leave_one_out(features)

    # ApLICAR SVC
    print('[INFO] Starting leave one out training...')
    count = 0
    sample_count = 0
    for train_set, test_set, label_train, label_test in zip(X_train, X_test, y_train, y_test):
        print('[INFO] Training sample {}/{}'.format(sample_count+1, len(y_train)))
        sample_count += 1

        # criar um objeto SVC (aqui eu posso ficar mudando o kernel. posso utilizar o rbf, poly, linear, sigmoid)
        svc = SVC(kernel='rbf', gamma='auto')

        # Treine o modelo
        svc.fit(train_set, label_train)

        # Avalie nos dados de teste
        new_list = []
        new_list.append(test_set)
        prediction = svc.predict(new_list)

        if prediction == label_test:
            count += 1

    accuracy = count / len(y_test)

    print('Accuracy using leave one out: {:.4f}'.format(accuracy))
