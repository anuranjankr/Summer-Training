import cv2
import numpy as np

'''
img=cv2.imread("parrot.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray_img,200,232,1)
#kernel=np.ones((5,5),np.uint8)
#dilation = cv2.dilate(thresh,kernel,iterations = 1)
#closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#print(thresh)
contours,hierarchy=cv2.findContours(thresh ,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_NONE)

print(len(contours))
max_area=0
index=0
for i in range(0,len(contours)):
    area=cv2.contourArea(contours[i])
    if area>=max_area:
        max_area=area
        index=i
print(max_area)
M=cv2.moments(contours[index])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print('centroid = ',cx,' ',cy)

rect = cv2.minAreaRect(contours[index])
box = cv2.boxPoints(rect)
box = np.int64(box)

cv2.drawContours(img, [box], -1, (0,0,255), 3)
#cv2.imshow("Gray",gray_img)
#cv2.imshow("Threshold_Image",thresh)
#cv2.imshow("Dilated_Image",closing)
cv2.imshow("Contour_Image",img)
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()
'''
'''
v=cv2.VideoCapture(0)
while True:
    ret,img=v.read()
    
    gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray_img,80,100,1)
    kernel=np.ones((5,5),np.uint8)
    dilation = cv2.dilate(thresh,kernel,iterations = 1)
    #closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    #print(thresh)
    contours,hierarchy=cv2.findContours(dilation ,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_NONE)
    rect = cv2.minAreaRect(contours[0])
    box = cv2.boxPoints(rect)
    box = np.int64(box)

    cv2.drawContours(img, [box], -1, (0,255,0), 3)
    #cv2.imshow("Gray",gray_img)
    #cv2.imshow("Threshold_Image",thresh)
    #cv2.imshow("Dilated_Image",dilation)
    #cv2.imshow("Contour_Image",img)
    cv2.imshow("Video",img)
    k=cv2.waitKey(1)    #here waitKey(1) is used to hold 1 milisec
    if k==ord('q'):
        break
v.release()
cv2.destroyAllWindows()
'''

##color filtering
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray_img,80,100,1)
    
    #lower_red = np.array([[[36,25,25]]])   #green
    #upper_red = np.array([[[70,255,255]]])
    lower_red = np.array([[[96,100,50]]])   #pink
    upper_red = np.array([[[255,230,255]]])
    #lower_red=cv2.cvtColor(lower_red,cv2.COLOR_BGR2HSV)
    #upper_red=cv2.cvtColor(upper_red,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    contours,hierarchy=cv2.findContours(thresh ,cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
    max_area= 0
    index=0
    for i in range(0,len(contours)):
        area=cv2.contourArea(contours[i])
        if area>=max_area:
            max_area=area
            index=i
    print(max_area)
    rect = cv2.minAreaRect(contours[index])
    box = cv2.boxPoints(rect)
    box = np.int64(box)

    cv2.drawContours(res, [box], -1, (0,0,255), 3)

    '''## slice the green
    imask = mask>0
    green = np.zeros_like(frame, np.uint8)
    green[imask] = frame[imask]'''
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
