import cv2 as cv
import numpy as np
img=cv.imread("image.jpg")
cv.imshow("image",img)


hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv img",hsv_img)


rgb_img=cv.cvtColor(hsv_img,cv.COLOR_HSV2RGB)
cv.imshow("RGB img",rgb_img)


blank=np.zeros(img.shape[:2],'uint8')
b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow("Blue img",blue)
cv.imshow("Green img",green)
cv.imshow("Red img",red)
