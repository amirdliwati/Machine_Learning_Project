## SuperVised Classification  Regression
from sklearn.ensemble import RandomForestClassifier

train_data = [[0,0],[1,0],[0,1],[1,1]]
train_labels = [0,1,1,0]
test_data =  [[0,0],[1,0],[0,1],[1,1]]

my_modle = RandomForestClassifier(n_estimators=1000)
my_modle.fit(train_data,train_labels)

print('\n The Model Score' , my_modle.score(train_data,train_labels))
print('Prediction', my_modle.predict(test_data))