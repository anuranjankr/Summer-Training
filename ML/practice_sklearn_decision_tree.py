#scikit-learn(sklearn) contains all ML algos
from sklearn.tree import DecisionTreeClassifier as DT

#datasets
b=[ [10,20], [30,40], [90,60], [51,99], [65,75], [45,51], [33,33], [35,34] ]
l=['bad','bad','good','good','good','bad','bad','good']

#classifier
clf=DT()

#training
train=clf.fit(b,l)

#prediction
result=train.predict([[40,51]])
print(result)
