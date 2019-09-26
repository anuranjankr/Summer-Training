from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('stock_market_data.csv')
f=np.array(df.drop('Date',axis=1))
l=df['Date']

clf=LinearRegression()
train=clf.fit(f,l)
result=train.predict(f)

print(result)

#Error
print("Error\nDesired\tPredicted\tError")
for i in range(0,len(f)):
    e=abs(int(result[i])-l[i])/l[i]
    print(l[i],'\t',int(result[i]),'\t',e*100)
    e=0
'''
# Plot outputs
plt.scatter(f, l,  color='black')
plt.plot(f, result, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
'''
