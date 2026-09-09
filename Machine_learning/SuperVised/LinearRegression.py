##Supervised Regression

import matplotlib.pyplot as matplot
from sklearn import linear_model

# input values
X = [[1.47],[1.50],[1.52],[1.55],[1.57],[1.60],[1.63],[1.65],[1.68],[1.70],[1.73],[1.75],[1.78],[1.80],[1.83]]
# Output Values
Y = [52.21,53.12,54.48,55.48,57.20,58.57,59.93,61.29,63.11,64.47,66.28,68.10,69.92,72.19,74.46]

test_data = [[1.3],[1.6],[1.9]]

Regression_model = linear_model.LinearRegression()
Regression_model.fit(X,Y)

print('Score:',Regression_model.score(X,Y))
print('Prediction :',Regression_model.predict(test_data))

#   Y = a * X + b
print('coefficient  ',Regression_model.coef_[0])
print('Intercept :  ',Regression_model.intercept_)

a = Regression_model.coef_[0]
b = Regression_model.intercept_

abLineValues = []
for i in X:
    abLineValues.append(a * i[0] + b)

matplot.scatter(X,Y)
matplot.plot(X, abLineValues,"r")
matplot.show()