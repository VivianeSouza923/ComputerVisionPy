import cv2

# ABRIR UMA IMAGEM COLORIDA
image = cv2.imread('copo-dos-lápis-coloridos-jpg-ep-4678664.jpg') #NOSSA IMAGEM VAI ESTAR DENTRO DA VARIÁVEL CHAMADA IMAGE.

# VISUALIZAR
cv2.imshow('Image', image) 
cv2.waitKey(0)

# E SALVAR
cv2.imwrite('saved_image.jpg', image)#NOSSA IMAGEM FOI SALVA COM UM NOME NOME "SAVED_IMAGE". SÓ OLHAR NA PASTA QUESTÃO1.