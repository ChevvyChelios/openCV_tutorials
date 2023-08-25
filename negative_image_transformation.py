
import cv2 as cv
import numpy as np

img = cv.imread('Photos/lady.jpg')

grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(grayed.shape)
L = 256
for i in range(685):
    for j in range(637):
        grayed[i,j] = L - 1 - grayed[i,j]

cv.imshow("Negative Image", grayed)
cv.waitKey(0)