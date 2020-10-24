#Utilizar o método Scale Invariant Feature Transform (SIFT) para detectar onde está um objeto conhecido à priori em uma imagem através dos keypoints detectados por este método. Desenhar os keypoints em comum e marcar o objeto procurado na imagem.

import cv2

# Abrir imagem colorida (vamos abrir tanto a imagem, quanto uma imagem só com logomarcas para procurar onde está o que queremos)
imcolor = cv2.imread('image.jpg')
imlogo = cv2.imread('logo.jpg')

# Transformar para tom de cinza (tanto a imagem normal, quanto a que contém as logos)
imcolor = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)
imlogo = cv2.cvtColor(imlogo, cv2.COLOR_BGR2GRAY)

# Create a SIFT detector (Obs.: in order to use sift descriptor you will have to install opencv-contrib
# from scratch. An alternative to that is to use opencv implementation called orb, it has almost the
# same result. To use orb, comment the lines with sift and uncomment the lines with orb.). Neste caso usamos o orb porque apesar de possuir o opencv_contrib, o meu dá erro.
#sift = cv2.xfeatures2d.SIFT_create()
orb = cv2.ORB_create()

# Find the keypoints and descriptors with SIFT
#keypoints_1, descriptors_1 = sift.detectAndCompute(image, None)
#keypoints_2, descriptors_2 = sift.detectAndCompute(logo, None)

#procurar os pontos-chaves e descritores com o orb (com o SIFT pra mim dá erro)
keypoints_1, descriptors_1 = orb.detectAndCompute(imcolor, None)
keypoints_2, descriptors_2 = orb.detectAndCompute(imlogo, None)

# Crie um objeto BFMatcher. cv2.NORM_HAMMING especifica a medição de distância a ser usada. Por padrão, é cv2.NORM_L2. É bom para SIFT, SURF etc (cv2.NORM_L1 também está lá). Para descritores baseados em strings binárias como ORB, BRIEF, BRISK etc, cv2.NORM_HAMMING deve ser usado, que usa a distância de Hamming como medida.o SEgundo parametro é uam variável booleana e ela por padrão é False. Se for True, Matcher apenas retorna apenas as correspondências com valor (i, j) de forma que o i-ésimo descritor no conjunto A tenha o j-ésimo descritor no conjunto B como a melhor correspondência e vice-versa.
objeto_BFMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Descritores de correspondÊncia. 
matches = objeto_BFMatcher.match(descriptors_1, descriptors_2)

# Draw only the first match. O resultado será o que sair da função drawMatches (ela recebe como parametro a imagem, o ponto-chave 1, a imagem com as logos, o ponto-chave 2, o None seria o lugar de uma terceira imagem de entrada e saída e por último os flags que nesse caso é 2)
resultado = cv2.drawMatches(imcolor, keypoints_1, imlogo, keypoints_2, matches[:2], None, flags=2)

# mostrar o resultado
cv2.imshow('Resultado', resultado)
cv2.waitKey(0)

# Salvar o resultado
cv2.imwrite('sift_result.jpg', resultado)