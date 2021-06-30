import cv2 as cv
import numpy as np

# Video capture obejct.
cap = cv.VideoCapture(0)
if not cap.isOpened():
   cap.open()

while True:
    # ret -> bool, frame -> camera frame.
    ret, frame = cap.read()

    # if frame is read correctly, ret is True.
    if not ret:
        print("Can't read frame")
        break
    
    # Camera capture.
    cv.imshow('Camera', frame)

    # Close camera with 'q' key press.
    if cv.waitKey(1) == ord('q'):
        break

# Release cap object.
cap.release()
# Destroy all existing windows.
cv.destroyAllWindows()