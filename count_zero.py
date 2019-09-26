import time as t
import numpy as np
arr1=np.identity(3)
print(arr1)
count=0
start=t.time()
for i in range(0,arr1.shape[0]):
    for j in range(0,arr1.shape[1]):
        if arr1[i][j]==0:
            count+=1
print("\nTime taken to compute : ",(t.time()-start)*1000)

start=t.time()
zero=arr1.size-np.count_nonzero(arr1)
print("\nTime taken to compute : ",(t.time()-start)*1000)


print("\nTotal no. of Zero ",count,zero)
    
