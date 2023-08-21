
import cv2 as cv

cap = cv.VideoCapture('Video/vid1.mp4')
# cap = cv.VideoCapture(0/1) # etc to access web cam etc

while True:
    isTrue, frame = cap.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
