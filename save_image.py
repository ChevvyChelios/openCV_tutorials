import cv2 as cv

img = cv.imread("images/cat1.jpg")

cv.imshow("Display image", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("cat1_saved.jpg", img)