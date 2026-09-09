import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

features = pd.read_csv('E:\Master_external/Data.csv')
features.head()
features

#convert each column to number
lbl=LabelEncoder()
features.gender=lbl.fit_transform(features.gender)
features.Nationality=lbl.fit_transform(features.Nationality)
features.PlaceofBirth=lbl.fit_transform(features.PlaceofBirth)
features.StageID=lbl.fit_transform(features.StageID)
features.GradeID=lbl.fit_transform(features.GradeID)
features.SectionID=lbl.fit_transform(features.SectionID)
features.Topic=lbl.fit_transform(features.Topic)
features.Semester=lbl.fit_transform(features.Semester)
features.Relation=lbl.fit_transform(features.Relation)
features.ParentAnsweringSurvey=lbl.fit_transform(features.ParentAnsweringSurvey)
features.ParentschoolSatisfaction=lbl.fit_transform(features.ParentschoolSatisfaction)
features.StudentAbsenceDays=lbl.fit_transform(features.StudentAbsenceDays)
features.Class=lbl.fit_transform(features.Class)

features

#extract the training data and the actual output
#first 16 column
X = features.iloc[:,:-1].values
X.shape
#lastColumn
y=features.iloc[:,-1].values
y.shape

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=44, shuffle =True)






