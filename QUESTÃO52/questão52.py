#Utilizar o método Speeded Up Robust Features (SURF) para detectar onde está um objeto conhecido à priori em uma imagem através dos keypoints detectados por este método. Desenhar os keypoints em comum e marcar o objeto procurado na imagem.

import cv2

#abrir uma imagem colorida
imcolor = cv2.imread('image.jpg')
imlogo = cv2.imread('logo.jpg')

#transformar para tom de cinza
imcolor = cv2.cvtColor(imcolor, cv2.COLOR_BGR2GRAY)
imlogo = cv2.cvtColor(imlogo, cv2.COLOR_BGR2GRAY)

# Create a SURF detector (Obs.: in order to use surf descriptor you will have to install opencv-contrib
# from scratch. An alternative to that is to use opencv implementation called orb, it has almost the
# same result. To use orb, comment the lines with surf and uncomment the lines with orb.)
#surf = cv2.xfeatures2d.SURF_create()

#criar a função orb
orb = cv2.ORB_create()

# Find the keypoints and descriptors with SIFT
#keypoints_1, descriptors_1 = surf.detectAndCompute(image, None)
#keypoints_2, descriptors_2 = surf.detectAndCompute(logo, None)


#Encontre os pontos-chave e descritores com orb
k1, d1 = orb.detectAndCompute(imcolor, None)
k2, d2 = orb.detectAndCompute(imlogo, None)

#CRIAR O OBJETO BFMatcher
objeto_BFMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)

#descritores de correspondÊncia
corresp = objeto_BFMatcher.match(d1, d2)

resultado = cv2.drawMatches(imcolor, k1, imlogo, k2, corresp[:2], None, flags=2)

cv2.imshow('Resultado', resultado)
cv2.waitKey(0)