# Logistic Regression - Classification

from sklearn.linear_model import LogisticRegression

Input_data = [[1.47],[1.50],[1.52],[1.55],[1.57],[1.60],[1.63],[1.65],[1.68],[1.70]]
OutPut_data = [1,1,1,1,1,0,0,0,0,0]

test_data = [[1.0],[1.6],[1.9]]

my_model = LogisticRegression()
my_model.fit(Input_data,OutPut_data)
my_model.score(Input_data,OutPut_data)

print('Score : ', my_model.score(Input_data,OutPut_data))

print('coefficient  ',my_model.coef_[0])
print('Intercept :  ',my_model.intercept_)

print('Prediction :',my_model.predict(test_data))

print(my_model.predict_proba(test_data))