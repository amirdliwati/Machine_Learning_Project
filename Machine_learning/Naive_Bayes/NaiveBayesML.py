##   SuperVised  Classification
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y = np.array([1,1,1,2,2,2])

my_model = GaussianNB()
my_model.fit(X,Y)

print(my_model.predict([[-0.8,-1]]))

my_model_PF = GaussianNB()
my_model_PF.partial_fit(X,Y,np.unique(Y))

print(my_model_PF.predict([[-0.8,-1]]))