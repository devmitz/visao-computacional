import cv2
image = cv2.imread('dog.jpg')
# Cria um retangulo azul por toda a largura da imagem
image[30:50, :] = (255, 0, 0)
# Cria um quadrado vermelho
image[50:150, 50:100] = (0, 255, 255)
# image[150:200, 0:150] = (0, 255, 0)
# Cria um retangulo amarelo por toda a altura da imagem
# image[:, 200:220] = (0, 255, 255)
# Cria um retangulo verde da linha 150 a 300 nas colunas 250 a 350
image[150:300, 250:350] = (0, 255, 0)
# Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a 350
# image[300:400, 50:150] = (255, 255, 0)
# Cria um quadrado branco
image[250:350, 300:400] = (255, 255, 255)
# Cria um quadrado preto
image[70:100, 300: 450] = (0, 0, 0)
cv2.imshow("Imagem alterada", image)
# cv2.imwrite("alterada.jpg", image)
cv2.waitKey(0)