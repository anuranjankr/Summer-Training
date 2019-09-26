def feature_map(pic):
    m=0
    f_map=np.eye(6)
    for i in range(0,pic.shape[0],3):
        n=0
        for j in range(0,pic.shape[1],3):
            mean_value=np.mean(np.dot(pic[i:i+3,j:j+3],np.eye(3)))#dot product ke liye upyukt matrix ka use karen
            f_map[m,n]=mean_value
            n=n+1
        m=m+1
        
    m=0
    f_map1=np.eye(3)
    for i in range(0,f_map.shape[0],2):
        n=0
        for j in range(0,f_map.shape[1],2):
            mean_value=np.mean(np.dot(f_map[i:i+2,j:j+2],np.eye(2)))#dot product ke liye upyukt matrix ka use karen
            f_map1[m,n]=mean_value
            n=n+1
        m=m+1
        
    return f_map1

def scale(pic):
    for i in range(0,pic.shape[0]):
        for j in range(0,pic.shape[1]):
            pic[i][j]/=255
    return pic

import cv2
import numpy as np

pic1=cv2.imread("pic1.png",0)#read image in gray format
pic2=cv2.imread("pic2.png",0)

#convert it into 20X20 array
pic1=cv2.resize(pic1,(18,18))
pic2=cv2.resize(pic2,(18,18))

#converting each pixel value between 0-1
pic1=scale(pic1)
pic2=scale(pic2)

#filters
fmap1=feature_map(pic1)
fmap2=feature_map(pic2)

fmap1=list(np.resize(fmap1,(1,9)))
fmap2=np.resize(fmap2,(1,9))
features=[]
features.append(fmap1)
features.append(fmap2)
labels=[['0'],['X']]
#train
from sklearn.neural_network import MLPClassifier
clf=MLPClassifier(hidden_layer_sizes=(10),solver='sgd',learning_rate_init=0.01,max_iter=45)
train=clf.fit(features,labels)




#result=train.predict(testing_set)


