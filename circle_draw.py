
import cv2 as cv
import numpy as np

# base creation
img = np.zeros((512,512,3), np.uint8)

#circle
cv.circle(img, (341,63),63,(0,255,0), -1)

cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()