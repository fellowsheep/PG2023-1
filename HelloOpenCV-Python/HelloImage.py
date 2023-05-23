import numpy as np
import cv2 as cv

img = cv.imread('baboon.png') #original
img2 = cv.imread('baboon.png') #copia para img modificada
print(img.shape) #exibe informações de dimensões e nro de canais

for i in range(img.shape[0]): #percorre linhas
	for j in range(img.shape[1]): #percorre colunas
		media = img.item(i,j,0) * 0.333 + img.item(i,j,1) * 0.333 + img.item(i,j,2) * 0.3333
		img2.itemset((i,j,0),media) # canal B
		img2.itemset((i,j,1),media) # canal G
		img2.itemset((i,j,2),media) # canal R
		
cv.imshow("Original",img)
cv.imshow("Grayscale",img2)

cv.waitKey(0)