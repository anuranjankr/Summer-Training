#scikit-learn(sklearn) contains all ML algos
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

#datasets
b=[ [10,20], [30,40], [90,60], [51,99], [65,75], [45,51], [33,33], [35,34] ]
b=np.array(b)
l=['bad','bad','good','good','good','bad','bad','good']
l=np.array(l)
#classifier
clf=KNeighborsClassifier(n_neighbors=3)#n_neighbors=k

#training
train=clf.fit(b,l)

#prediction
result=train.predict([[45,99]])
print(result)
