import cv2 as cv
import numpy as np

img = cv.imread('Photos/Cats.jpg')
# img = cv.imread('Photos/cats 2.jpg')
# img = cv.imread('images/girl1.webp')
# cv.imshow('Original', img)

# blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# simple threshholding
# threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# threshhold = 150(user input)
# cv.imshow('Simple threshhold', thresh)

# threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple threshhold inverse', thresh_inv)

# Adaptive Thresholding
adapt_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 7)
# adapt_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholding', adapt_thresh)

cv.waitKey(0)