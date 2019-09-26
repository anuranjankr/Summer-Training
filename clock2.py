import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math
fig=plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7,6.5)

sx=[5,5]
sy=[5,9]
length=4
ax=plt.axes([0,10,0,10])
cir=plt.Circle((0,0),3)

def animate(i):
    val_sin=math.sin((math.pi/180)*6*i)
    val_cos=math.cos((math.pi/180)*6*i)
    i=5+length*val_sin
    j=5+length*val_cos
    x=[sx[0],i]
    y=[sy[0],j]
    ax.plot(x,y,'r')
    ax.plot(sx,sy,'g')
    return ax

anim=animation.FuncAnimation(fig,animate,frames=360,interval=60,blit=True)

plt.show()
