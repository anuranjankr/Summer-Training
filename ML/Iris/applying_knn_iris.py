import numpy as np
import xlrd
from sklearn.neighbors import KNeighborsClassifier

rb=xlrd.open_workbook('Iris_data_modified.xls')
rs2=rb.sheet_by_index(2)

features=[]
for i in range(1,rs2.nrows):
    #features.append(rs2.row_values(i)[1:5])
    lst=[]
    for j in range(1,rs2.ncols-1):
        lst.append(float(rs2.cell_value(i,j)))
    features.append(lst)
    lst=[]
    
features=np.array(features)

labels=[]
for i in range(1,rs2.nrows):
    labels.append(rs2.row_values(i)[5:6][0])

labels=np.array(labels)

clf=KNeighborsClassifier(n_neighbors=30)

train=clf.fit(features,labels)

rs1=rb.sheet_by_index(1)

training_set=[]
for i in range(0,rs1.nrows):
    #training_set.append(rs1.row_values(i)[1:5])
    lst=[]
    for j in range(1,rs1.ncols-1):
        lst.append(float(rs1.cell_value(i,j)))
    training_set.append(lst)
    lst=[]

#print(training_set)
training_set=np.array(training_set)

result=train.predict(training_set)
print(result)

