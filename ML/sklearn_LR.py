from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x=np.array([[1],[2],[3],[4],[5.1],[6],[7],[8.4],[9],[10]])
y=np.array([1,2.2,2.9,5,4.7,5.3,7.2,8.9,9,10.1])

clf=LinearRegression()
train=clf.fit(x,y)
x_test=[[5],[7],[4.3],[8]]
result=train.predict(x_test)
print(result)

# Plot outputs
plt.scatter(np.ravel(x), y,  color='black') #list 0th element
plt.plot(np.ravel(x_test), result, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

