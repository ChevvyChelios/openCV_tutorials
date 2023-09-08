
import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("original", img)

# blank = np.zeros((427,640), dtype='uint8')
blank = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow("blue", blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merged = cv.merge([b,g,r])
# merged = cv.merge([b,blank,blank])
# cv.imshow('Merged image', merged)

cv.waitKey(0)