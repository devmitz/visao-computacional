import numpy as np
import cv2

img = cv2.imread('dog.jpg')
img = img[::2, ::2]  # Diminui a imagem
suave = np.vstack([
    np.hstack([img,
               cv2.medianBlur(img, 3),
               cv2.medianBlur(img, 5)]),

    np.hstack([cv2.medianBlur(img, 7),
               cv2.medianBlur(img, 9),
               cv2.medianBlur(img, 11)]),
])
cv2.imshow("Imagem original e suavisadas pela mediana", suave)
cv2.waitKey(0)
