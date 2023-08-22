
import cv2 as cv

im1 = cv.imread("Faces/train/Jerry_Seinfield/3.jpg")
im2 = cv.imread("Faces/train/Ben_Afflek/7.jpg")

wh = 300
re_im2 = cv.resize(im2, (wh,wh))

# new_im = cv.add(im1,re_im2)
#       dst = src1 * alpha + src2 * beta + gamma
new_im = cv.addWeighted(im1, 0.3, re_im2, 0.8, 0)

cv.imshow("image Blending", new_im)
# cv.imwrite("Add_saved2.jpg", new_im)

cv.waitKey(0)
cv.destroyAllWindows()