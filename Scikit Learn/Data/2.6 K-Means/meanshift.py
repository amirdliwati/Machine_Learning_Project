# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:29:00 2020

@author: Ahmed
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:57:04 2020
@author: Ahmed
"""
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
# #############################################################################


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

#dataset = (dataset - dataset.mean()) / dataset.std()

#extract the training data and the actual output


X = dataset.iloc[:,2:].values

print(X.shape)
# #############################################################################
# Compute clustering with MeanShift

# The following bandwidth can be automatically detected using
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=400)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
labels
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)

# #############################################################################
# Plot result
import matplotlib.pyplot as plt
from itertools import cycle

plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()

print('KMeansModel labels are : ' , labels)

mydict = {i: np.where(labels == i)[0] for i in range(n_clusters_)}

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

