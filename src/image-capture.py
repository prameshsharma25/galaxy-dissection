import cv2 as cv
import sys

img = cv.imread('/home/prameshsharma25/Desktop/Projects/galaxy-dissection/assets/galaxy.jpg')

if img is None:
    sys.exit('Couldn\'t read image.')

img = cv.resize(img, (224, 224))

cv.imshow('galaxy', img)
cv.waitKey(0)