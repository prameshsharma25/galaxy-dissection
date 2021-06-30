import numpy as np
import cv2 as cv

img = np.ones((224, 224, 3)) * 255

def draw_circle(img, img_shape, radius, color, thickness=8):
    return cv.circle(img, img_shape, radius, color, thickness)

red_circle  = draw_circle(img, (int(img.shape[0]/2), int(img.shape[1]/4)), 40, (0, 0, 255))
green_circle = draw_circle(img, (int(img.shape[0]/4), int(img.shape[1]*(2/3))), 40, (0, 255, 0))
blue_circle = draw_circle(img, (int(img.shape[0]*(3/4)), int(img.shape[1]*(2/3))), 40, (255, 0, 0))
cv.imshow('cv2-logo', img)
cv.waitKey(0)