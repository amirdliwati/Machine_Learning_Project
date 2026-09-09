##Supervised

import numpy as np
import matplotlib.pyplot as matplot
from sklearn import svm
from matplotlib import style

style.use('ggplot')

my_input = np.array([[2,3],[6,6],[2.6,3],[7,8],[3.5,5],[6,11]])
my_output= [0,1,0,1,0,1]

my_model = svm.SVC(kernel='linear',C=1.0)
my_model.fit(my_input,my_output)

print('SVC predict[0.5,0.8] :',my_model.predict([[0.5,0.8]]))
print('SVC predict[8.5,10] :',my_model.predict([[8.5,10]]))
print('[:,0] :  ',my_input[:,0])
print('[:,1] :  ',my_input[:,1])

w = my_model.coef_[0]
print('Coefficiant : ',w)

a = -w[0]/w[1]
xx = np.linspace(0,12)
yy = a*xx - my_model.intercept_[0]/w[1]
h0 = matplot.plot(xx,yy,'k-',label='non wighted div')

matplot.scatter(my_input[:,0],my_input[:,1],c=my_output)
matplot.scatter(0.5,0.8,c='r')
matplot.scatter(8.5,10 ,c='r')
matplot.legend()
matplot.show()
