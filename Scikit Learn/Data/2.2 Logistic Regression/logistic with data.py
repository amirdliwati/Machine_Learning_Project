import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
 
df = pd.read_csv('E:\Master_external/Data.csv')

######### K-Means ######################3

from sklearn.cluster import KMeans
lbl=LabelEncoder()
df.Class=lbl.fit_transform(df.Class)

categorical_features = ['gender', 'Nationality', 'PlaceofBirth', 'StageID', 'GradeID',
       'SectionID', 'Topic', 'Semester', 'Relation','ParentAnsweringSurvey', 'ParentschoolSatisfaction',
       'StudentAbsenceDays']
X = pd.get_dummies(df.iloc[:,0:16], columns = categorical_features)
S_sc=StandardScaler()

X = S_sc.fit_transform(X)

y=df.iloc[:,-1].values
y

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,random_state=33,shuffle='true')


logreg = LogisticRegression()
logreg.fit(x_train , y_train)
result= logreg.predict(x_test)
print("the accuracy is : ", accuracy_score(y_test , result))
 
conf = confusion_matrix(y_test , result)
print('confusion matrix \n',  conf)
 
 