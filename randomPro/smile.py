
import cv2 as cv
import numpy as np

# base creation
img = np.ones((500,700,3), np.uint8) * 255

font = cv.FONT_HERSHEY_SIMPLEX
# cv.putText(img,"GANTETSUSAI",(200,100),font, 1, (0,0,0), 4, cv.LINE_4)
cv.putText(img,"SMILE PLEASE",(100,200),font, 2, (0,0,0), 4, cv.LINE_8)

pt1 = (199,309)
pt2 = (299,299)
pt3 = (479,219)
pt4 = (325,320)
# bpt1 = pt1
# bpt2 = pt2
# cv.circle(img,bpt1,2,(0,0,255),-1)
# cv.circle(img,bpt2,2,(0,0,255),-1)
# cv.line(img,bpt1,bpt2, (255,0,0),1)
cv.ellipse(img,(249,304), (49,5), 175, 0,180, (0,0,0),2)

# bpt1 = pt2
# bpt2 = pt3
# cv.circle(img,bpt1,2,(0,0,255),-1)
# cv.circle(img,bpt2,2,(0,0,255),-1)
# cv.line(img,bpt1,bpt2, (255,0,0),1)
cv.ellipse(img,(389,259), (97,10), 156, 0,180, (0,0,0),2)

# bpt1 = pt1
# bpt2 = pt4
# cv.circle(img,bpt1,2,(0,0,255),-1)
# cv.circle(img,bpt2,2,(0,0,255),-1)
# cv.line(img,bpt1,bpt2, (255,0,0),1)
cv.ellipse(img,(262,315), (62,2), 185, 0,180, (0,0,0),2)

# bpt1 = pt4
# bpt2 = pt3
# cv.circle(img,bpt1,2,(0,0,255),-1)
# cv.circle(img,bpt2,2,(0,0,255),-1)
# cv.line(img,bpt1,bpt2, (255,0,0),1)
cv.ellipse(img,(402,269), (91,2), 147, 0,180, (0,0,0),2)

cv.line(img,pt2,pt4,(0,0,0),1)
# Left Teeth
cv.line(img,(226,301),(250,310),(0,0,0),1)
cv.line(img,(254,300),(275,312),(0,0,0),1)
cv.line(img,(275,299),(296,315),(0,0,0),1)

# Right teeth
cv.line(img,(320,281),(345,305),(0,0,0),1)
cv.line(img,(340,271),(360,295),(0,0,0),1)
cv.line(img,(363,261),(380,280),(0,0,0),1)
cv.line(img,(386,250),(401,267),(0,0,0),1)
cv.line(img,(413,238),(423,252),(0,0,0),1)
cv.line(img,(439,228),(446,238),(0,0,0),1)
# cv.circle(img,(439,228),3,(255,0,0),-1)
# cv.circle(img,(446,238),3,(0,0,255),-1)

# cv.line(img,pt1,pt2,(0,0,255),1)
# cv.line(img,pt2,pt3,(0,0,255),1)
# cv.line(img,pt3,pt4,(0,0,255),1)
# cv.line(img,pt4,pt1,(0,0,255),1)


cv.imshow("Give me a smile", img)

cv.waitKey(0)
cv.destroyAllWindows()