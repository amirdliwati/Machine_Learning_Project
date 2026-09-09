
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder



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
X = dataset.iloc[:,:-1].values
y= dataset.iloc[:,-1].values


from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp = imp.fit(X)
X= imp.transform(X)



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
regressor.fit(X_train, y_train)

regressor.score(X_train, y_train)

# Predicting a new result
y_pred = regressor.predict(X_test)




