from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import xlrd

rb=xlrd.open_workbook('Iris_data_modified.xls')
rs2=rb.sheet_by_index(2)

features=[]
for i in range(1,rs2.nrows):
    lst=[]
    for j in range(1,rs2.ncols-1):
        lst.append(float(rs2.cell_value(i,j)))
    features.append(lst)
    lst=[]
    
features=np.array(features)

rs1=rb.sheet_by_index(1)
testing_set=[]
for i in range(0,rs1.nrows):
    lst=[]
    for j in range(1,rs1.ncols-1):
        lst.append(float(rs1.cell_value(i,j)))
    testing_set.append(lst)
    lst=[]



kmeans=KMeans(n_clusters=3).fit(features)#remove random then check
result=kmeans.predict(testing_set)
print(result)
