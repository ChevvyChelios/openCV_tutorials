import cv2 as cv
import numpy as np

img = cv.imread("images/pic2.jpg")
img = cv.resize(img,(int(img.shape[1]*0.3), int(img.shape[0]*0.3)), interpolation=cv.INTER_AREA)
cv.imshow("Chicken", img)

# Flipped
flip = cv.flip(img, 1) # 1,0,-1 == vertical, horizontal, both
cv.imshow("Flipped",flip)

cv.waitKey(0)
cv.destroyAllWindows()