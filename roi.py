
import cv2 as cv
import numpy as np

# base creation
person = cv.imread("images/man4.webp")
# print(person.shape)

face = person[250:350,350:700]

person[360:460,350:700] = face

cv.imshow("Person", person)

cv.waitKey(0)
cv.destroyAllWindows()