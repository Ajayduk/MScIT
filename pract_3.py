import cv2 as cv
import numpy as np
img=cv.imread("image.jpg")
cv.imshow("image",img)

height,width,dim=img.shape

resize_img=cv.resize(img,(width//2,height//2))
cv.imshow("resize_img",resize_img)


crop_img=img[50:200,100:300]
cv.imshow("crop_img",crop_img)


def translate(img,x,y):
    transMatrix=np.float32([[1,0,x],[0,1,y]])
    return cv.warpAffine(img,transMatrix,(width,height))

translate_img=translate(img,-100,-200)
cv.imshow("translate_img",translate_img)


def rotate(img,angle,rotPoint=None):
    if(rotPoint is None) :
        scale=1.0
        rotPoint=height//2,width//2
        rotMatrix=cv.getRotationMatrix2D(rotPoint,angle,scale)

        return cv.warpAffine(img,rotMatrix,(width,height))

rotation_img=rotate(img,25,None)
cv.imshow("rotation_img",rotation_img)


flip_img=cv.flip(img,1)
cv.imshow("flip_img",flip_img)


