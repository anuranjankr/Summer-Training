#    KNN FOR 1 Feature
marks=[12,19,32,36,62,45,98,78,71]
grade=['F','F','F','Avg','Avg','Avg','G','G','G']

'''
def min_list(min_lst,temp_dist,k):
    for i in (0,k):
        min_lst.append(min(temp_dist))
        temp_dist.pop(temp_dist.index(min(temp_dist)))
    return min_lst
'''

while 1:
    uin=int(input("Enter Your Marks : "))
    k=int(input("Enter K in KNN algo : "))
    
    dist=[]
    for m in marks:
        dist.append(abs(uin-m))
        
    '''    
    min_lst=[]
    i=0
    j=3
    for i in range(0,3):
        temp_dist=dist[i:j]
        min_lst=min_list(min_lst,temp_dist,k)
        i=j
        j+=3
    
    print(min_lst)
    
    avg_lst=[]
    for i in range(0,3):
        avg=0
        avg=(min_lst[0]+min_lst[1])/2
        avg_lst.append(avg)
        for j in range(0,k):
            min_lst.pop(0)
        print(min_lst)
        print("Avg: ",avg_lst)
     '''
    temp_dist=[]
    avg_lst=[]
    for i in range(0,9,3):
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
