import cv2
import numpy as np
import random
'''
    #Gray Color Image
img=cv2.imread("flower1.jpeg",0)
cv2.imshow("Image",img)
k=cv2.waitKey(0)
if k==ord('q'):           # 27 is for esc key
    cv2.destroyAllWindows()
'''
'''
    #Gray Color Image 2
img=cv2.imread("flower1.jpeg")  #3d array (A*B*3)
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #2d array(A*B)
cv2.imshow("Image",gray_img)
k=cv2.waitKey(0)
if k==ord('q'):           # 27 is for esc key
    cv2.destroyAllWindows()
'''
'''
    #(500 X 500) white window
j=np.ones([500,500])
cv2.imshow("Image",j)
k=cv2.waitKey(0)
if k==ord('q'):           # 27 is for esc key
    cv2.destroyAllWindows()
    #(500 X 500) black window
j=np.zeros([500,500])
cv2.imshow("Image",j)
k=cv2.waitKey(0)
if k==ord('q'):           # 27 is for esc key
    cv2.destroyAllWindows()
'''
    #on a black window draw a white block of (5X5)
req_window=np.zeros([500,500])
r_int=random.randint(0,495)
#for i in range(r_int,r_int+6):
 #   for j in range(r_int,r_int+6):
  #      req_window[i][j]=req_window[i][j]+1
req_window[r_int:r_int+5,r_int:r_int+6]+=1
cv2.imshow('Game Window',req_window)
key=cv2.waitKey(0)
if key==ord('q'):
    cv2.destroyAllWindows()
    
