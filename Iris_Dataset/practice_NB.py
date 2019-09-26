import pandas as pd
import numpy as np
df=pd.read_csv("/home/anuranjan/Summer Training/ML/stock_market_data.csv")
dataset=np.array(df)
#label=df['date']
#datasets=df.get_values()
label=np.ravel(dataset[:,0:1])
features=dataset[:,1:]
print(features)

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.3, random_state=1) 

# training the model on training set 
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB() 
gnb.fit(X_train, y_train) 


# making predictions on the testing set 
y_pred = gnb.predict(X_test) 
print(y_pred)
# comparing actual response values (y_test) with predicted response values (y_pred) 
from sklearn import metrics 
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
