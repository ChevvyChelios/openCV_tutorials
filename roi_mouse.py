
import cv2 as cv
import numpy as np

# base creation
person = cv.imread("images/man4.webp")
# print(person.shape)

# select roi
r = cv.selectROI("Select the area", person)

#crop image
cropped_image = person[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

cv.imshow("Cropped Image", cropped_image)

cv.waitKey(0)
cv.destroyAllWindows()