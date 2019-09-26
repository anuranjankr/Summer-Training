import cv2
img=cv2.imread("flower1.jpeg")

def img_border(img,b,color):
    '''
    This function takes 3 arguments
    img=image
    b=border_size
    color=color{i.e, blue green or red}
    '''
    y,x=img.shape[:2]   #y=rows and x=cols
    for i in range(0,3):
        img[0:y,x-b:x,i]=color[i]   #right
        img[0:y,0:b,i]=color[i]     #left
        img[0:b,0:x,i]=color[i]     #top
        img[y-b:y,0:x,i]=color[i]   #bottom
    return img
def display_img(img):
    '''
    This function is used to display a image.
    It takes image variable(in which image file was read) as an input.
    for Eg:
        display_img(img1)
        where
        img1=cv2.imread("filename")
    To close window press key 'q' on keyboard.
    '''
    cv2.imshow('My Image',img)
    key=cv2.waitKey(0)
    if key==ord('q'):
        cv2.destroyAllWindows()

b=int(input("Enter the Border size around Image : "))
while True:
    uin=input("Enter\n1.Blue\n2.Green\n3.Red\n4.Exit \t: ")
    if uin=='1':
        color=[255,0,0]
        img=img_border(img,b,color)
        display_img(img)
    elif uin=='2':
        color=[0,255,0]
        img=img_border(img,b,color)
        display_img(img)
    elif uin=='3':
        color=[0,0,255]
        img=img_border(img,b,color)
        display_img(img)
    elif uin=='4':
        break
    else:
        print("Wrong Input")
        
'''
        Previous Program

import cv2
a=cv2.imread('flower1.jpeg')

#cv2.imshow('My Image',a)
color=input("Enter\n1.Blue\n2.Green\n3.Red \t: ")
y,x=a.shape[:2]
b=5
color=input("Enter\n1.Blue\n2.Green\n3.Red \t: ")
y,x=a.shape[:2]
b=5
if color=='2':
    #rigtht
    a[0:y,x-b:x,1]=255
    a[0:y,x-b:x,0]=0
    a[0:y,x-b:x,2]=0
    #left
    a[0:y,0:b,1]=255
    a[0:y,0:b,0]=0
    a[0:y,0:b,2]=0
    #top
    a[0:b,0:x,1]=255
    a[0:b,0:x,0]=0
    a[0:b,0:x,2]=0
    #bottom
    a[y-b:y,0:x,1]=255
    a[y-b:y,0:x,0]=0
    a[y-b:y,0:x,2]=0
elif color=='1':
    #rigtht
    a[0:y,x-b:x,1]=0
    a[0:y,x-b:x,0]=255
    a[0:y,x-b:x,2]=0
    #left
    a[0:y,0:b,1]=0
    a[0:y,0:b,0]=255
    a[0:y,0:b,2]=0
    #top
    a[0:b,0:x,1]=0
    a[0:b,0:x,0]=255
    a[0:b,0:x,2]=0
    #bottom
    a[y-b:y,0:x,1]=0
    a[y-b:y,0:x,0]=255
    a[y-b:y,0:x,2]=0
elif color=='3':
    #rigtht
    a[0:y,x-b:x,1]=0
    a[0:y,x-b:x,0]=0
    a[0:y,x-b:x,2]=255
    #left
    a[0:y,0:b,1]=0
    a[0:y,0:b,0]=0
    a[0:y,0:b,2]=255
    #top
    a[0:b,0:x,1]=0
    a[0:b,0:x,0]=0
    a[0:b,0:x,2]=255
    #bottom
    a[y-b:y,0:x,1]=0
    a[y-b:y,0:x,0]=0
    a[y-b:y,0:x,2]=255
else:
    print("Wrong Input")

cv2.imshow('My Image',a)
    
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()


'''
