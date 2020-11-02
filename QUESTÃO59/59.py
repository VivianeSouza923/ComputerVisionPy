#Faça a matriz de confusão para as questões de 53 a 58.

import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

#criar a função plot confusion matrix
def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.get_cmap('Greens')):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # matriz de confusão computacional
    cm = confusion_matrix(y_true, y_pred)
    # Use apenas os rótulos que aparecem nos dados
    classes = unique_labels(y_true, y_pred)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # Nós queremos mostrar todos os ticks
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... e rotule-os com as respectivas entradas da lista
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Gire os rótulos de escala e defina seu alinhamento.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Faça um loop nas dimensões dos dados e crie anotações de texto.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


# Obtenha os nomes dos arquivos em uma lista
files = ['true_and_predict_' + str(num) + '.csv' for num in range(53, 59)]

# Percorrer arquivos
for file in files:
    print(file)
    with open(file, 'r') as infile:
        # ler o arquivo csv
        read = csv.reader(infile, delimiter=',')

        # Obtenha os dados dos arquivos lidos
        data = []
        for row in read:
            data.append(row)

        # Defina os nomes das classes
        class_names = ['0', '1', '2']

        # Crie uma lista para rótulos verdadeiros e preditivos
        true = [int(x) for x in data[0]]
        pred = [int(x) for x in data[1]]

        # Trace a matriz de confusão
        plot_confusion_matrix(true, pred, classes=class_names,
                              title='Confusion matrix, without normalization')
        plt.show()