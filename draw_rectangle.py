
import cv2 as cv
import numpy as np

img = np.ones((500,500,3), np.uint8) * 255

pt1 = (499,0)
pt2 = (249,249)

cv.rectangle(img, pt1,pt2, (0,0,0), 2, lineType=cv.LINE_8, shift=0)

cv.imshow('rectangle', img)

cv.waitKey(0)
cv.destroyAllWindows()