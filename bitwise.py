import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

# img = cv.imread('Photos/cat.jpg')

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cir = cv.circle(blank.copy(), (200,200), 200, 255, -1)

# cv.imshow('Rectangle', rect)
# cv.imshow('Circle', cir)

# bitwise AND
# b_and = cv.bitwise_and(rect, cir)
# cv.imshow('Bitwise AND', b_and)

# bitwise OR
# b_or = cv.bitwise_or(rect, cir)
# cv.imshow('Bitwise OR', b_or)

# bitwise XOR
b_xor = cv.bitwise_xor(rect, cir)
cv.imshow('Bitwise XOR', b_xor)

# bitwise NOT
b_not = cv.bitwise_not(cir)
cv.imshow('Bitwise NOT', b_not)

cv.waitKey(0)