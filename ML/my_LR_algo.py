import numpy as np
import math
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5.1,6,7,8.4,9,10])
y=np.array([1,2.2,2.9,5,4.7,5.3,7.2,8.9,9,10.1])

x_bar=np.mean(x)
y_bar=np.mean(y)

#calulation of 'm' slope

numerator=0
denominator=0
for i in range(len(x)):
    numerator+=(x[i]-x_bar)*(y[i]-y_bar)
    denominator+=math.pow(x[i]-x_bar,2)     #(x[i]-x_bar)**2

m=numerator/denominator

#calculation for 'c' intercept

c=(y_bar-(m*x_bar))

#prediction
uin=float(input("Give an input number : "))
print("Predicted Value : ",((m*uin)+c))

#plot
u = np.linspace(0.5,10.5,100)
v = m*u + c
plt.plot(u, v, '-r')
plt.title('Linear Regression')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.scatter(x,y,color='g')
plt.grid()
plt.show()
