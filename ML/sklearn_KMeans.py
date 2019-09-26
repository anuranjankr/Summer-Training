from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
'''
X = np.array([[1, 2], [1, 4], [1, 0],[10, 2], [10, 4], [10, 0],[11,3],[7,9],[1,2],[4,19],[7,13]])
for i in range(0,10):
    kmeans=KMeans(n_clusters=3,random_state=5).fit(X)#remove random then check
    result=kmeans.predict([[0, 0]])
    print(result)
'''
df=pd.read_csv("Mall_Customers.csv")
x=np.array(df)
np.random.shuffle(x)
f=x[:,3:5][0:140]
#f=np.array(df.drop(['CustomerID','Age'],axis=1))
t=x[:,3:5][140:201]
kmeans=KMeans(n_clusters=2).fit(f)#remove random then check
result=kmeans.predict(t)
for i in range(0,55):
    if result[i]==0:
        print(x[:,1][i])
print(result)
