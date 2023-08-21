
import cv2 as cv
import numpy as np

# base creation
img = np.ones((300,300,3), np.uint8) * 255

pts = np.array([[49,149],[149,49],[249,149],[149,249]], np.int32)
cv.polylines(img,[pts], True, (0,0,255), 3)

cv.imshow("There's Text here", img)

cv.waitKey(0)
cv.destroyAllWindows()