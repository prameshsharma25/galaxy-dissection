import cv2 as cv
import matplotlib.pyplot as plt

ix, iy = 0, 0
draw = False

img = cv.imread('/home/prameshsharma25/Desktop/Projects/galaxy-dissection/assets/galaxy.jpg')
if img is None:
    print('Image was not read.')
    exit()

if img.shape[0] > 512 or img.shape[1] > 512:
    img = cv.resize(img, (512, 512))
    
def crop_image(event, x, y, flags, param):
    global ix, iy, draw
    
    if event == cv.EVENT_LBUTTONDBLCLK:
        if not draw:
            draw = True
            ix, iy = x, y
        else:
            draw = False
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)

    if event == cv.EVENT_MOUSEMOVE:
        if draw == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)

cv.namedWindow('New Image')
cv.setMouseCallback('New Image', crop_image)
    
# Event Loop.
while True:
    cv.imshow('New Image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()