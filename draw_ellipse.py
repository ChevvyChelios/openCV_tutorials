
import cv2 as cv
import numpy as np

img = np.ones((500,500,3), np.uint8) * 255

center = (249,249)
axes = (180,50)
angle = 40
startAngle = 0
endAngle = 360

cv.ellipse(img,center,axes,angle,startAngle,endAngle,(0,0,0), 2)

cv.imshow('Ellipse', img)

cv.waitKey(0)
cv.destroyAllWindows()