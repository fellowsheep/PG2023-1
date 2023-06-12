import numpy as np
import cv2 as cv

img = cv.imread('baboon.png') #original

imgGrayscale =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)

imgBlurred5x5 = cv.blur(imgGrayscale,(5,5))
imgBlurred15x15 = cv.blur(imgGrayscale,(15,15))

#Gaussian Blur -- Coloque lado a lado com o Blur normal pra ver a diferença
imgGaussianBlurred5x5 = cv.GaussianBlur(imgGrayscale,(5,5),0)
imgGaussianBlurred15x15 = cv.GaussianBlur(imgGrayscale,(15,15),0)

imgCanny1 = cv.Canny(imgGrayscale,50,100)
imgCanny2 = cv.Canny(imgBlurred5x5,50,100)
imgCanny3 = cv.Canny(imgBlurred15x15,50,100)
imgCanny4 = cv.Canny(imgGaussianBlurred15x15,50,100)

kernel = np.ones((3,3),np.uint8)
#Dilatação e Erosão -- teste com imagens diferentes!
imgDilation = cv.dilate(imgCanny2,kernel,iterations = 1)
imgErosion = cv.erode(imgDilation,kernel,iterations = 1)

cv.imshow("Imagem Grayscale",imgGrayscale)
#cv.imshow("Imagem Blurred - 5x5",imgBlurred5x5)
cv.imshow("Imagem Blurred - 15x15",imgBlurred15x15)

#cv.imshow("Imagem Gaussian Blurred - 5x5",imgGaussianBlurred5x5)
cv.imshow("Imagem Gaussian Blurred - 15x15",imgGaussianBlurred15x15)


#cv.imshow("Deteccao Canny - Img Grayscale",imgCanny1)
#cv.imshow("Deteccao Canny - Blur 5x5",imgCanny2)
cv.imshow("Deteccao Canny - Blur 15x15",imgCanny3)
cv.imshow("Deteccao Canny - Gaussia Blur 15x15",imgCanny4)

cv.waitKey(0)
cv.destroyAllWindows()