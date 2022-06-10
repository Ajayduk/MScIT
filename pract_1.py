import cv2 as cv
import numpy as np

#Create blank screeen default color will be black
blank=np.zeros([500,500,3],'uint8')

#Change color to white
blank[:]=255,255,255

w,h,d=blank.shape

#Rectangle require screen, starting_point, ending_point,color,thinkness
rect=cv.rectangle(blank,(0,0),(w//2,h//2),(255,0,0),2)


#Circle Require Screen,cener_point,radius,color,thikness
circle=cv.circle(blank,(w//2,h//2),50,(255,0,0),2)
cv.imshow("blank",blank)
