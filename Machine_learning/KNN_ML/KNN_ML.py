##  K- Nearest Neighbors(KNN)   SuperVised Classification  Regression

from sklearn.neighbors import KNeighborsClassifier

X = [[0],[1],[2],[3]]
Y = [0,0,1,1]

my_model = KNeighborsClassifier(n_neighbors=3)
my_model.fit(X,Y)

print(my_model.predict([[1.1]]))
print(my_model.predict_proba([[0.9]]))
