# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:37:15 2020

@author: Ahmed
"""
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.cluster import MiniBatchKMeans
# #############################################################################
#read the dataset
dataset = pd.read_csv('E:\Master_external/Data.csv')
dataset.head()
print("feature shape: ", dataset.shape)
dataset.describe()
lbl=LabelEncoder()

#convert each column to number
dataset.gender=lbl.fit_transform(dataset.gender)
dataset.Nationality=lbl.fit_transform(dataset.Nationality)
dataset.PlaceofBirth=lbl.fit_transform(dataset.PlaceofBirth)
dataset.StageID=lbl.fit_transform(dataset.StageID)
dataset.GradeID=lbl.fit_transform(dataset.GradeID)
dataset.SectionID=lbl.fit_transform(dataset.SectionID)
dataset.Topic=lbl.fit_transform(dataset.Topic)
dataset.Semester=lbl.fit_transform(dataset.Semester)
dataset.Relation=lbl.fit_transform(dataset.Relation)
dataset.ParentAnsweringSurvey=lbl.fit_transform(dataset.ParentAnsweringSurvey)
dataset.ParentschoolSatisfaction=lbl.fit_transform(dataset.ParentschoolSatisfaction)
dataset.StudentAbsenceDays=lbl.fit_transform(dataset.StudentAbsenceDays)
dataset.Class=lbl.fit_transform(dataset.Class)

#extract the training data and the actual output
X = dataset.iloc[:,2:].values



MiniBatchKMeansModel = MiniBatchKMeans(n_clusters=3,batch_size=30,init='random') #also can be random
kmean=MiniBatchKMeansModel.fit(X)

print('KMeansModel Train Score is : ' , kmean.score(X))
print('KMeansModel labels are : ' , kmean.labels_)
print('KMeansModel intertia is : ' , kmean.inertia_)
print('KMeansModel No. of iteration is : ' , kmean.n_iter_)

mydict = {i: np.where(kmean.labels_ == i)[0] for i in range(kmean.n_clusters)}

# Transform this dictionary into list (if you need a list as result)
dictlist = []
for key, value in mydict.items():
    temp = [key,value]
    dictlist.append(temp)

#########  SVM Classifier ###########
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


for i in range(len(mydict)):
    dataset=X[mydict[i]]
    X_train2=dataset[:,:-1]
    y_train2=dataset[:,-1]
    
    #create object for SVC
    svm = SVC(kernel='rbf', C=10.0, random_state=33)
    X_train, X_test, y_train, y_test = train_test_split(X_train2, y_train2, test_size=0.2, random_state=33)
    svm.fit(X_train, y_train)
    
    print(( X_train.shape, X_test.shape, y_train.shape, y_test.shape))
    
    #predict the test data
    y_pred = svm.predict(X_test)
    print("the confution matrix is : ",confusion_matrix(y_test, y_pred))
    print('Misclassified samples: %d' % (y_test != y_pred).sum())
    print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))  
