
import cv2 as cv
import numpy as np
from math import log

img = cv.imread('Photos/lady.jpg')

grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(grayed.shape)
c = 30
temp = grayed
for i in range(685):
    for j in range(637):
        # grayed[i,j] = c * log(1 + temp[i,j])
        grayed[i,j] = c * np.log(1 + temp[i,j])

max_val = np.max(grayed)
min_val = np.min(grayed)
r = 256

for i in range(685):
    for j in range(637):
        grayed[i,j] = ((grayed[i,j] - min_val) / (max_val - min_val)) * r

cv.imshow("Enhanched Image", grayed)
cv.waitKey(0)