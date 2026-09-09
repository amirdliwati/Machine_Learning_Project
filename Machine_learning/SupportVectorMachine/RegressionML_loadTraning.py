##Supervised

import numpy as np
import matplotlib.pyplot as matplot
from sklearn import svm
from matplotlib import style
from sklearn.externals import joblib

# style.use('ggplot')

# my_input = np.array([[2,3],[6,6],[2.6,3],[7,8],[3.5,5],[6,11]])
# my_output= [0,1,0,1,0,1]

my_model = joblib.load('Machine_learning/SupportVectorMachine/Mymodel_save.sav')

print('SVR predict[0.5,0.8] :',my_model.predict([[0.5,0.8]]))
print('SVR predict[8.5,10] :',my_model.predict([[8.5,10]]))


# matplot.scatter(my_input[:,0],my_input[:,1],c=my_output)
# matplot.scatter(0.5,0.8,c='r')
# matplot.scatter(8.5,10 ,c='r')
# matplot.show()
