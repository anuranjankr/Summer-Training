import matplotlib.pyplot as plt
import matplotlib.style
import numpy as np
from time import ctime

def clock_circle():
    '''
    This function provides coodinates for a circle
    and 12 dots as on a analog clock.
    '''
    #defining radius of circle
    r=5
    #Coordinates for circle
    t=np.arange(0,2*np.pi,.01)
    x=r*np.sin(t)
    y=r*np.cos(t)
    #Coordinates for 12 dots
    t2=np.linspace(0,2*np.pi,13)
    x2=r*np.sin(t2)
    y2=r*np.cos(t2)
    return x,y,x2,y2
    
def position_of_hands(degree,length,hms,x,y):
    '''
    This function takes 5 arguments are as follows:
    degree=movment of hands on its ticks
    length=length of hands
    hms=hour/min/sec
    x=x-coordinates of hand
    y=y-coordinates of hand
    '''
    val_sin=np.sin((np.pi/180)*degree*hms)
    val_cos=np.cos((np.pi/180)*degree*hms)
    i=length*val_sin
    j=length*val_cos
    x=[x[0],i]
    y=[y[0],j]
    return x,y

#Storing Current time in Variable h m s
h=float(ctime()[11:13])
m=float(ctime()[14:16])
s=float(ctime()[17:19])

#Defining sec,min,hrs vector
vec_sx=[0,0]
vec_sy=[0,4.7]
mag_s=4.7

vec_mx=[0,0]
vec_my=[0,3.8]
mag_m=3.8

vec_hx=[0,0]
vec_hy=[0,3]
mag_h=3

#Calculation for hour to get accurate hand position
h=h+m/60

#Plotting graph
plt.axis([-6,6,-6,6])

sx,sy=position_of_hands(6,mag_s,s,vec_sx,vec_sy)
plt.plot(sx,sy,'r')

mx,my=position_of_hands(6,mag_m,m,vec_mx,vec_my)
plt.plot(mx,my,'g')

hx,hy=position_of_hands(30,mag_h,h,vec_hx,vec_hy)
plt.plot(hx,hy,'b')

x,y,x2,y2=clock_circle()
plt.plot(x2,y2,'bo')
plt.plot(x,y,'k')

plt.show()

