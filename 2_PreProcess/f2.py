import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('dave.png', 0) #读取灰度图

laplacian = cv.Laplacian(img,cv.CV_64F)  #拉普拉斯滤波
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5) #x方向上的sobel滤波
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5) #y方向上的sobel滤波

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()


"""
cv.imshow("gray", img)
cv.imshow("laplacian", laplacian)
cv.imshow("sobel_x", sobelx)
cv.imshow("sobel_y", sobely)

cv.waitKey(0)
cv.destroyAllWindows()
"""