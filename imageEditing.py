import cv2 as cv

img = cv.imread("Photos/park.jpg")
# img = cv.imread("images/girl1.webp")
# img = cv.resize(img,(int(img.shape[1]*0.5), int(img.shape[0]*0.5)), interpolation=cv.INTER_AREA)

cv.imshow("Picture", img)

# Convert to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)   # the ksize should be an odd number (oddNUM, oddNUM)
cv.imshow("Blur", blur)

# Edge Cascade
# canny = cv.Canny(img, 125,175)
canny = cv.Canny(blur, 125,175)
cv.imshow("Canny Edge", canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("Resize", resize)

# Cropped
# cropped = img[100:200, 100:120]
cropped = img[80:200, 70:180]
cv.imshow("Cropped",cropped)

cv.waitKey(0)
cv.destroyAllWindows()