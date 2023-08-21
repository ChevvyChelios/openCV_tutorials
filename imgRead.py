import cv2 as cv
import sys

img = cv.imread("images/cat1.jpg")
img2 = cv.imread("images/man1.jpg", cv.IMREAD_GRAYSCALE)

# if img is None:
#     sys.exit("Could mot read the image")
# cv.imshow("Display window", img)

cv.imshow("Cat", img)
# cv.imshow("Man", img2)
cv.waitKey(0)

# print(img.shape)
# print(img2.shape)
# print(img)
# print(img2)