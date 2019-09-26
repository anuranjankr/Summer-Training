import cv2
from random import randint
import numpy as np
m=300
req_window=np.zeros([m,m])
r_int_f=0

def move(window,x,y):
    req_window[x-3:x+3,y-3:y+3]+=1
    if (r_int_f>=x-3 and r_int_f<x+3) and (r_int_f>=y-3 and r_int_f<y+3):
        window=food(window,x,y)
    return window
    
def food(window,x,y):
    global r_int_f
    while True:
        r_int_f=randint(0,m-2)
        if (r_int_f>=x-3 and r_int_f<x+3) and (r_int_f>=y-3 and r_int_f<y+3):
            continue
        else:
            window[r_int_f:r_int_f+3,r_int_f:r_int_f+3]+=1
            break
    return window

def init_window(window,x,y):
    window[x-3:x+3,y-3:y+3]+=1
    window=food(req_window,x,y)
    return window

x=randint(5,m-5)
y=randint(5,m-5)
req_window=init_window(req_window,x,y)

while True:
    cv2.imshow('Game Window',req_window)
    key=cv2.waitKey(0)
    if key==ord('w'):
        req_window[x-3:x+3,y-3:y+3]*=0
        x-=2
        req_window=move(req_window,x,y)
    if key==ord('s'):
        req_window[x-3:x+3,y-3:y+3]*=0
        x+=2
        req_window=move(req_window,x,y)
    if key==ord('d'):
        req_window[x-3:x+3,y-3:y+3]*=0
        y+=2
        req_window=move(req_window,x,y)
    if key==ord('f'):
        req_window[x-3:x+3,y-3:y+3]*=0
        y-=2
        req_window=move(req_window,x,y)
    if key==ord('q'):
        cv2.destroyAllWindows()
        break
