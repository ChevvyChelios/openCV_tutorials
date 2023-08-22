
import cv2 as cv

im1 = cv.imread("Faces/train/Jerry_Seinfield/3.jpg")
im2 = cv.imread("Faces/train/Ben_Afflek/7.jpg")

# print(im1.shape)
# print(im2.shape)
wh = 300
re_im2 = cv.resize(im2, (wh,wh))
# print(re_im2.shape)

# cv.imshow("Faces", im1)
# cv.imshow("Ben", re_im2)

# new_im = cv.add(im1,re_im2)
new_im = cv.add(re_im2,im1)
cv.imshow("2 image summmed", new_im)
cv.imwrite("Add_saved2.jpg", new_im)

cv.waitKey(0)
cv.destroyAllWindows()