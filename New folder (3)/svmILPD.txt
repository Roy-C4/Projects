import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Here we have loaded the dataset using pandas library
dataset = pd.read_csv("ILPD.csv")

# Data Preprocessing starts here
X = dataset.iloc[:,0:9].values
y = dataset.iloc[:,10].values

# Data Gender encoded
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()


# Train-test split
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)       
X_test = sc_X.transform(X_test)

# Classifier trained 
from sklearn.svm import SVC
svmclassifier = SVC(kernel = 'rbf',random_state = 0)
svmclassifier.fit(X_train,y_train)

# Classifier tested
y_pred = svmclassifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)



from sklearn.metrics import precision_score, accuracy_score, recall_score
precision = precision_score(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)
recall = recall_score(y_test,y_pred)

print("precision: ",precision)
print("accuracy: ",accuracy)
print("recall: ",recall)
