import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img = cv.imread('Photos/Cats.jpg')
img = cv.imread('Photos/cats 2.jpg')
# img = cv.imread('images/girl1.webp')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img, mask=circle)
cv.imshow('Mask', masked)

# Grayscale histogram
# gray_hist = cv.calcHist([img], [0], circle, [256], [0,256])
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# color histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)