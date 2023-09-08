
import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("original", img)

# Averging
# avg = cv.blur(img, (7,7))
# cv.imshow('Average blur', avg)

# # Gaussan Blur
gauss = cv.GaussianBlur(img, (7,7),-1)
cv.imshow('Gaussian Blur', gauss)

# # Median Blur
# median = cv.medianBlur(img, 7)
# cv.imshow('Median Blur', median)

# Bilateral
bilat = cv.bilateralFilter(img,5,75,-75)
cv.imshow('Bilateral image', bilat)

cv.waitKey(0)