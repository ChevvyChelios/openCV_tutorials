import cv2 as cv
import numpy as np

img = cv.imread("images/pic2.jpg")
img = cv.resize(img,(int(img.shape[1]*0.3), int(img.shape[0]*0.3)), interpolation=cv.INTER_AREA)
# cv.imshow("Chicken", img)

# traslation asix (x,y)
def translate(img, x,y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # translation matrix
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> left
# -y --> up
# x --> right
# y --> down
translated = translate(img, -100, 100)
cv.imshow("Translated", translated)

# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = ((width // 2),( height // 2))
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)
rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotated_rotated', rotated_rotated)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# Flipped
flip = cv.flip(img, 1) # 0,1,-1 == vertical, horizontal, both
cv.imshow("Flipped",flip)

# croppd
# cropped = img[100:400, 100:400]
# cv.imshow("Cropped", cropped)

cv.waitKey(0)
cv.destroyAllWindows()