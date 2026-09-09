## SuperVised  Classification - Regression
from sklearn import tree

train_data = [[0,0],[1,0],[0,1],[1,1]]
train_labels = [0,1,1,0]
test_data =  [[0,0],[1,0],[0,1],[1,1]]

my_modle = tree.DecisionTreeClassifier(criterion='gini')
my_modle.fit(train_data,train_labels)

print('\n The Model Score' , my_modle.score(train_data,train_labels))
print('Prediction', my_modle.predict(test_data))


## Regression

X = [[0,0],[2,2]]
Y = [0.5,2.5]

my_modle2 = tree.DecisionTreeRegressor()
my_modle2.fit(X,Y)
print('Score : ' ,my_modle2.score(X,Y))
print('Prediction : ', my_modle2.predict([[1,1]]))