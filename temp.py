import cv2 as cv
import numpy as np

# base creation
# img = np.ones((500,500,3), np.uint8) * 255
# ar = np.zeros((10,10,3), np.uint8) * 255
# print(ar)
img = cv.imread("images/girl1.webp")
print(img.shape)
print(int(img.shape[1]*0.5), int(img.shape[0]*0.5))
# cv.imshow("White board", img)

# cv.waitKey(0)
# cv.destroyAllWindows()