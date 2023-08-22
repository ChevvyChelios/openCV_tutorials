
import cv2 as cv

img = cv.imread("images/boy1.jpg")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# cv.imshow("Image", gray)
# cv.imshow("Image", hsv)
cv.imshow("Image", lab)
cv.waitKey(0)
cv.destroyAllWindows()