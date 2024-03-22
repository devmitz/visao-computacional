# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread('dog.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1])  # largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0])  # altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

verde = (0, 255, 0)
fonte = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(imagem, 'lisan al-gaib', (15, 100), fonte,
            2, verde, 2, cv2.LINE_AA)

# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0)  # espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
# cv2.imwrite("saida.jpg", imagem)
