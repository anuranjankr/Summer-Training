import cv2
import numpy as np
import pynput

cap = cv2.VideoCapture(0)
#lower_red = np.array([[[36,25,25]]])   #green
#upper_red = np.array([[[70,255,255]]])
lower_pink = np.array([[[96,100,50]]])   #pink
upper_pink = np.array([[[255,230,255]]])
    
while True:
    lst=[]
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray_img,80,100,1)
    
    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    contours,hierarchy=cv2.findContours(thresh ,cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
    max_area= 0
    index=0
    for i in range(0,len(contours)):
        lst.append(cv2.contourArea(contours[i]))
    max_area=max(lst)
    print(max_area)
    index=lst.index(max_area)
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
