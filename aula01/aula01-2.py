import cv2
imagem = cv2.imread('dog.jpg')
for y in range(0, imagem.shape[0], 10):  # percorre linhas
    for x in range(0, imagem.shape[1], 10):  # percorre colunas
        imagem[y:y+5, x: x+5] = (0, 0, 255)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
