##  K- Nearest Neighbors(KNN)   SuperVised Classification  Regression
####    iris Example

from sklearn import neighbors,datasets
import numpy as np
import pylab as pl

iris = datasets.load_iris()
X = iris.data[:,:2] #only take first tow features
Y = iris.target

h = 0.2 # step size in mesh


my_model = KNeighborsClassifier()
my_model.fit(X,Y)
