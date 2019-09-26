import numpy as np
import xlwt
import xlrd
import random

rb=xlrd.open_workbook('Iris.xls')
rs=rb.sheet_by_index(0)

data_list=[]
for i in range(1,rs.nrows):
    data_list.append(rs.row_values(i))

dataset=np.array(data_list)     # Array
sec1_idx=49
sec2_idx=99
sec3_idx=149
count=0

del_data_set=[]

for i in range(0,5):
    index=random.randint(0,sec1_idx-count)
    del_data_set.append(list(dataset[index]))
    dataset=np.delete(dataset,index,axis=0)
    count+=1
sec1_idx-=count
for i in range(0,5):
    index=random.randint(sec1_idx,sec2_idx-count)
    del_data_set.append(list(dataset[index]))
    dataset=np.delete(dataset,index,axis=0)
    count+=1
sec2_idx-=count
for i in range(0,5):
    index=random.randint(sec2_idx,sec3_idx-count)
    del_data_set.append(list(dataset[index]))
    dataset=np.delete(dataset,index,axis=0)
    count+=1



nwb=xlwt.Workbook()
nws1=nwb.add_sheet('Sheet1_Original_data')
nws2=nwb.add_sheet('Sheet2_Random_data')
nws3=nwb.add_sheet('Sheet3_Remaining_data')
'''
for i in range(0,rs.nrows-1):
    for j in range(0,rs.ncols):
        nws1.write(i,j,data_list[i][j])  # Error has been solved (Edited rs.nrows-1 instead rs.nrows)
'''
temp_datalist=np.array(data_list)
for i in range(0,temp_datalist.shape[0]):
    for j in range(0,temp_datalist.shape[1]):
        nws1.write(i,j,data_list[i][j])
        
temp_del_data_set=np.array(del_data_set)
for i in range(0,temp_del_data_set.shape[0]):
    for j in range(0,temp_del_data_set.shape[1]):
        nws2.write(i,j,del_data_set[i][j])

for i in range(0,dataset.shape[0]):
    for j in range(0,dataset.shape[1]):
        nws3.write(i,j,dataset[i][j])

nwb.save('Iris_data_modified.xls')

print("Every Line Executed Successfully")
