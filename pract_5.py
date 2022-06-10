import cv2 as cv
import numpy as np

blank=np.zeros((400,400),'uint8')

rect=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("rect",rect)
cv.imshow("circle",circle)


bi_and=cv.bitwise_and(rect,circle)
cv.imshow("bi_and",bi_and)


bi_or=cv.bitwise_or(rect,circle)
cv.imshow("bi_or",bi_or)


bi_xor=cv.bitwise_xor(rect,circle)
cv.imshow("bi_xor",bi_xor)


img=cv.imread("image.jpg")
cv.imshow("image",img)

img_not=cv.bitwise_not(img)
cv.imshow("img_not",img_not)


