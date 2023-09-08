
import cv2 as cv
import numpy as np

cap = cv.VideoCapture('Video/vid1.mp4')
# cap = cv.VideoCapture(0/1) # etc to access web cam etc
# Rescale size 
def rescaleFrame(frame, scale=0.75):
    # for video, image and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = cap.read()
    re_fr = rescaleFrame(frame, scale=0.5)
    # cv.imshow('video', frame)
    cv.imshow('video', re_fr)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
