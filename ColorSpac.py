
import cv2 as cv
import matplotlib.pyplot as plt

# img = cv.imread("images/boy1.jpg")
img = cv.imread("Photos/park.jpg")
# cv.imshow("original", img)

# plt.imshow(img)
# plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# cv.imshow("gray", gray)
# cv.imshow("hsv", hsv)
cv.imshow("lab", lab)
# cv.imshow("rgb", rgb)

# HSV to BGR
# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSV ---> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB ---> BGR', lab_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
cv.destroyAllWindows()