#   KNN FOR 2 Features
import math

#marks=[[12,19],[13,7],[32,24],[36,65],[62,31],[45,55],[98,62],[78,74],[71,86]]
#grade=['F','F','F','Avg','Avg','Avg','G','G','G']

marks=[ [10,20], [30,40], [45,51], [90,60], [51,99], [65,75] ]
grade=['bad','bad','bad','good','good','good']


while 1:
    x=int(input("Enter Your 1st Marks : "))
    y=int(input("Enter Your 2nd Marks : "))
    k=int(input("Enter K in KNN algo : "))
    
    dist=[]
    for m in marks:
        dist.append(math.sqrt(math.pow(m[0]-x,2)+math.pow(m[1]-y,2)))

    temp_dist=[]
    avg_lst=[]
    for i in range(0,6,3):
        for j in range(0,3):
            j+=i
            temp_dist.append(dist[j])
        avg=0
        for l in range(0,k):
            avg+=min(temp_dist)
            temp_dist.pop(temp_dist.index(min(temp_dist)))
        temp_dist=[]
        avg/=k
        avg_lst.append(avg)
    
    min_index=avg_lst.index(min(avg_lst))
    
    print("Your Grade is : ",grade[min_index*3])
    
    ip=input("Enter 0 to stop : ")
    if ip=='0':
        break
