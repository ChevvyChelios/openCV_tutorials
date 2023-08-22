
import cv2 as cv
import numpy as np

img = np.zeros((500,500,3), np.uint8)

pnts = np.array([[250,99],[349,149],[349,249],[250,299],[250,99]])

pnts2 = np.array([[248,99],[248,299],[149,249],[149,149],[248,99]])

# cv.polylines(img,[pnts],True,(0,0,255),thickness=-1)
# cv.polylines(img,[pnts2],True,(255,0,0),thickness=-1)
cv.fillPoly(img,[pnts],(0,0,255))
cv.fillPoly(img,[pnts2],(255,0,0))

cv.imshow("polygon", img)

cv.waitKey(0)
cv.destroyAllWindows()