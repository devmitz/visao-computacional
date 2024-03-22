import numpy as np
import cv2
imagem = cv2.imread('dog.jpg')
vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)
cv2.line(imagem, (0, 0), (100, 200), verde)
cv2.line(imagem, (300, 200), (150, 150), vermelho, 5)
cv2.rectangle(imagem, (20, 20), (120, 120), azul, 10)
cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1)
(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
for raio in range(0, 175, 15):
    cv2.circle(imagem, (X, Y), raio, vermelho)

fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem, 'lisan al-gaib', (15, 65), fonte,
            2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)
