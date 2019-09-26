from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
import xlrd

rb=xlrd.open_workbook('Iris_data_modified.xls')
rs2=rb.sheet_by_index(2)

features=[]
labels=[]
for i in range(1,rs2.nrows):
    lst=[]
    for j in range(1,rs2.ncols-1):
        lst.append(float(rs2.cell_value(i,j)))
    features.append(lst)
    labels.append(rs2.row_values(i)[5:6][0])
    lst=[]
    
features=np.array(features)
labels=np.array(labels)

rs1=rb.sheet_by_index(1)
testing_set=[]
test=[]
for i in range(0,rs1.nrows):
    lst=[]
    for j in range(1,rs1.ncols-1):
        lst.append(float(rs1.cell_value(i,j)))
    testing_set.append(lst)
    test.append(rs1.row_values(i)[5:6][0])
    lst=[]

testing_set=np.array(testing_set)
test=np.array(test)


clf=MLPClassifier(hidden_layer_sizes=(10),solver='sgd',learning_rate_init=0.01,max_iter=45)
train=clf.fit(features,labels)
result=train.predict(testing_set)
print(result)

count=0
for i in range(0,rs1.nrows):
    if result[i]==test[i]:
        count+=1
print("Accuracy : ",(count/rs1.nrows)*100)
