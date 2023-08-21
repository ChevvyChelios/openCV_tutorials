
import cv2 as cv

# Rescale size 
def rescaleFrame(frame, scale=0.75):
    # for video, image and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Resize resolution 
def changeRes(width, height):
    # for live video
    capture.set(3,width)
    capture.set(4,height)
    

# Reading image
# img = cv.imread('Photos/cat.jpg')
# cv.imshow("CAT", img)
# resized_image = rescaleFrame(img, scale=.5)
# cv.imshow("Image", resized_image)

# Reading Videos
capture = cv.VideoCapture('Video/vid1.mp4')

while True:
    isTrue, frame = capture.read()
    # frame_resized = rescaleFrame(frame)
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('video', frame)
    cv.imshow('video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
# cv.waitKey(0)
cv.destroyAllWindows()