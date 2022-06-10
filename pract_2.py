import cv2 as cv

img=cv.imread("image.jpg")
cv.imshow("image",img)


gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image",gray_img)

blur_img=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blur Image",blur_img)


canny_img=cv.Canny(blur_img,150,170)
cv.imshow("Canny Image",canny_img)

dilate_img=cv.dilate(canny_img,(3,3),iterations=3)
cv.imshow("Dialate Image",dilate_img)


erode_img=cv.erode(canny_img,(3,3),iterations=3)
cv.imshow("Erode Image",erode_img)
