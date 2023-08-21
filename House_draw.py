
import cv2 as cv
import numpy as np

# base creation
img = np.ones((300,300,3), np.uint8) * 255

pt1 = (150,0)
pt2 = (50,170)
pt3 = (250,170)
pt4 = (100,299)
pt5 = (200,299)

#circle
# cv.circle(img, (center point),radius,(color), fill)
cv.circle(img, pt1, 2, (0,0,255), -1)
cv.circle(img, pt2, 2, (0,0,255), -1)
cv.circle(img, pt3, 2, (0,0,255), -1)
# cv.circle(img, pt4, 2, (0,0,255), -1)
# cv.circle(img, pt5, 2, (0,0,255), -1)

# triangle_cnt = np.array([pt1,pt2,pt4,pt5,pt3])
triangle_cnt = np.array([pt1,pt2,pt3])

cv.drawContours(img, [triangle_cnt], 0, (0,255,0), -1)
cv.rectangle(img, (50,170), (250,299), (0,0,255), -1)

cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()