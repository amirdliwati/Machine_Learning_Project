##   SuperVised , UnSuperVised Multi Layer
import numpy as np
from sklearn.neural_network import MLPClassifier

XORNetwork = np.array([0,0,0,1,1,0,1,1]).reshape(4,2)
output = np.array([0,1,1,0]).reshape(4,)

my_model = MLPClassifier(activation='relu',max_iter=10000,hidden_layer_sizes=(8,2))
my_model.fit(XORNetwork,output)

print('Score : ',my_model.score(XORNetwork,output))
print('prediction : ',my_model.predict(XORNetwork))
print('expected : ',np.array([0,1,1,0]))

