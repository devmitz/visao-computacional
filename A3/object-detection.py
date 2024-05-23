import numpy as np
import cv2
import mahotas

# Função para facilitar a escrita nas imagens
def escreve(img, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10, 20), fonte, 0.5, cor, 0, cv2.LINE_AA)

imgColorida = cv2.imread('p.jpg')  # Carregamento da imagem
imgColorida = imgColorida[::2, ::2]

# Se necessário, o redimensionamento da imagem pode vir aqui.

# Passo 1: Conversão para tons de cinza
img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)

# Passo 2: Blur/Suavização da imagem
suave = cv2.GaussianBlur(img, (11, 11), 0)

# Passo 3: Binarização resultando em pixels brancos e pretos
T = mahotas.thresholding.otsu(suave)
bin = suave.copy()
bin[bin > T] = 255
bin[bin <= T] = 0
bin = cv2.bitwise_not(bin)

# Aplicando erosão e dilatação
# kernel = np.ones((3, 3), np.uint8)
# bin = cv2.erode(bin, kernel, iterations=2)
# bin = cv2.dilate(bin, kernel, iterations=2)

# Passo 4: Detecção de bordas com Canny
bordas = cv2.Canny(bin, 70, 150)

# Passo 5: Identificação e contagem dos contornos da imagem
# cv2.RETR_EXTERNAL = conta apenas os contornos externos
objetos, _ = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtragem de contornos por área
min_area = 500  # Define o mínimo de área para um objeto ser considerado
objetos_filtrados = [cnt for cnt in objetos if cv2.contourArea(cnt) > min_area]

# A variável _ (lixo) recebe dados que não são utilizados
escreve(img, "Imagem em tons de cinza", 0)
escreve(suave, "Suavizacao com Blur", 0)
escreve(bin, "Binarizacao com Metodo Otsu", 255)
escreve(bordas, "Detector de bordas Canny", 255)

temp = np.vstack([
    np.hstack([img, suave]),
    np.hstack([bin, bordas])
])
cv2.imshow("Quantidade de objetos: "+str(len(objetos_filtrados)), temp)
cv2.waitKey(0)

imgC2 = imgColorida.copy()
cv2.imshow("Imagem Original", imgColorida)

cv2.drawContours(imgC2, objetos_filtrados, -1, (0, 0, 255), 2)
escreve(imgC2, str(len(objetos_filtrados))+" objetos encontrados!")
cv2.imshow("Resultado", imgC2)
cv2.waitKey(0)
