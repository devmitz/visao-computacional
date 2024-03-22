import cv2
import numpy as np

img = cv2.imread('dog.jpg')
img_orig = cv2.imread('dog.jpg')
img_rato = cv2.imread('imagem.jpg')

fonte = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'LISAN AL-GAIB', (15, 100), fonte,
            2, (255, 255, 255), 2, cv2.LINE_AA)

img = cv2.flip(img, 1)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converte
img_rato = cv2.cvtColor(img_rato, cv2.COLOR_BGR2GRAY)  # converte

suave = cv2.GaussianBlur(img, (7, 7), 0)  # aplica blur
suave_rato = cv2.GaussianBlur(img_rato, (7, 7), 0)  # aplica blur

bin1 = cv2.adaptiveThreshold(suave, 255,
                             cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)

bin2 = cv2.adaptiveThreshold(suave_rato, 255,
                             cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)


cv2.imshow("Binarização adaptativa da imagem", bin1)
cv2.imshow("LISAN AL-GAIB", img_orig)

cv2.waitKey(0)
