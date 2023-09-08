
import cv2 as cv
import numpy as np

img = np.zeros((500,500,3), np.uint8)
# img = np.ones((512,512,3), np.uint8) * 255

# img[:] = 0,0,0
# img[:] = 255,255,255

# cv.rectangle(img,(0,0),(249,249), (0,0,255), 2)
cv.rectangle(img,(0,0),(img.shape[1]//2, img.shape[0]//2), (0,0,255), 2)

# draw a circle
cv.circle(img,(img.shape[1]//2, img.shape[0]//2),40, (200,0,160), 3)

# draw a line
cv.line(img, (499,0), (0,499), (255,0,0), 5)

# direct change
img[200:300, 300:400] = 17,135,45

# put text on the image
cv.putText(img, "This is akrom", (150,350), cv.FONT_HERSHEY_PLAIN, 2, (12,196,241), 4)

cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()