import numpy as np
import xlrd
from sklearn.svm import SVC

rb=xlrd.open_workbook('Iris_data_modified.xls')
rs2=rb.sheet_by_index(2)

features=[]
labels=[]
for i in range(1,rs2.nrows):
    #features.append(rs2.row_values(i)[1:5])
    lst=[]
    for j in range(1,rs2.ncols-1):
        lst.append(float(rs2.cell_value(i,j)))
    features.append(lst)
    labels.append(rs2.row_values(i)[5:6][0])
    lst=[]
    
features=np.array(features)
labels=np.array(labels)

#clf=SVC(kernel='linear')
clf=SVC(C=1000,kernel='poly',degree=3,gamma='auto')
#clf=SVC(kernel='rbf',gamma='scale')
#clf=SVC(kernel='sigmoid',gamma='scale')

train=clf.fit(features,labels)

rs1=rb.sheet_by_index(1)

testing_set=[]
test=[]
for i in range(0,rs1.nrows):
    #training_set.append(rs1.row_values(i)[1:5])
    lst=[]
    for j in range(1,rs1.ncols-1):
        lst.append(float(rs1.cell_value(i,j)))
    testing_set.append(lst)
    test.append(rs1.row_values(i)[5:6][0])
    lst=[]

#print(training_set)
testing_set=np.array(testing_set)
test=np.array(test)

result=train.predict(testing_set)

count=0
for i in range(0,rs1.nrows):
    if result[i]==test[i]:
        count+=1
print("Accuracy : ",(count/rs1.nrows)*100)

