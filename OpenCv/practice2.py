import cv2
import numpy as np
'''
        #finding threshold of an image
img=cv2.imread("flower1.jpeg",0)
thres=cv2.threshold(img,70,255,0)[1] #cv2.threshold returns two values(T/F,res_img)
cv2.imshow("Gray",img)
cv2.imshow("Threshold_Image",thres)
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()
'''
'''
    #finding contour and drawing contour
a=cv2.imread("untitled.png")
gray_img=cv2.imread("untitled.png",0)
ret,thresh=cv2.threshold(gray_img,200,255,1)
print(thresh)
contours,hierarchy=cv2.findContours(thresh ,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(a, contours, -1, (0,0,255), 3)
cv2.imshow("Gray",gray_img)
cv2.imshow("Threshold_Image",thresh)
cv2.imshow("Contour_Image",a)
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()
'''
img=cv2.imread("parrot.jpg")

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray_img,200,232,1)
kernel=np.ones((5,5),np.uint8)
#dilation = cv2.dilate(thresh,kernel,iterations = 1)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
print(thresh)
contours,hierarchy=cv2.findContours(closing ,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,0,255), 3)
print(len(contours))
cv2.imshow("Gray",gray_img)
cv2.imshow("Threshold_Image",thresh)
cv2.imshow("Dilated_Image",closing)
cv2.imshow("Contour_Image",img)
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()
