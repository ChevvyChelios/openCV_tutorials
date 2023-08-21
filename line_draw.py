

# '+' sign using line() function

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv.line(img, (0,255), (511,255), (0,0,255), 10)
cv.line(img, (255,0), (255,511), (0,0,255), 10)

cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()