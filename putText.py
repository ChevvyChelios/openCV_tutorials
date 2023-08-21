
import cv2 as cv
import numpy as np

# base creation
img = np.ones((300,300,3), np.uint8) * 255

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "I want to sleep", (30,99), font, 1, (0,0,0), 4, cv.LINE_4)

cv.imshow("There's Text here", img)

cv.waitKey(0)
cv.destroyAllWindows()