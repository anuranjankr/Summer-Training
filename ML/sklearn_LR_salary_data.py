from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Salary_Data.csv')
dataset=np.array(df)
np.random.shuffle(dataset)
#f=dataset[:,0][0:25].reshape(-1,1)
#l=dataset[:,1][0:25]
f=dataset[:,0].reshape(-1,1)
l=dataset[:,1]

clf=LinearRegression()
train=clf.fit(f,l)
#x_test=dataset[:,0][25:30].reshape(-1,1)
#result=train.predict(x_test)
result=train.predict(f)

#print("check output\n",dataset[25:30])
print("check output\n",dataset)
print(result)

#Error
print("Error\nDesired     \tPredicted    \t\tError")
for i in range(0,len(f)):
    e=abs(result[i]-dataset[:,1][i])/dataset[:,1][i]
    print(dataset[:,1][i],'\t',result[i],'\t',e*100)
    e=0

# Plot outputs
plt.scatter(np.ravel(f), l,  color='black')
plt.plot(np.ravel(f), result, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

