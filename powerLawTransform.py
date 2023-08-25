
import cv2 as cv
import numpy as np

img = cv.imread('Photos/lady.jpg')

grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(grayed.shape)
c = 5
p = 0.7
for i in range(685):
    for j in range(637):
        grayed[i,j] = c * (grayed[i,j] ** p)
print(grayed)

cv.imshow("Enhanched Image", grayed)
cv.waitKey(0)