import cv2 as cv
import numpy as np

img = cv.imread("images/girl2.webp")
img = cv.resize(img,(int(img.shape[1]*0.4), int(img.shape[0]*0.4)), interpolation=cv.INTER_AREA)
cv.imshow("Girl", img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow("blank", blank)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(blur, 125,125)
# canny = cv.Canny(gray, 125,125)
# cv.imshow("canny", canny)

# ret, thresh = cv.threshold(gray, 130,255, cv.THRESH_BINARY)
# cv.imshow("thresh", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found.')

cv.drawContours(blank, contours, -1, (10,100,200), 1)
cv.imshow('contour', blank)

cv.waitKey(0)
cv.destroyAllWindows()