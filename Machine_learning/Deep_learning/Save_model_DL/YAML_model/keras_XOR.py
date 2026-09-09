##   keras deep learning XOR
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras import backend as k
from keras.utils.vis_utils import plot_model
import numpy as np
import pickle as pl

x = np.array([[0,0],[1,0],[0,1],[1,1]])
y = np.array([[0],[1],[1],[0]])

my_model = Sequential()
my_model.add(Dense(8,input_dim=2,activation = k.tanh))
my_model.add(Dense(1,activation=k.sigmoid))
my_model.compile(SGD(lr=0.1),loss='binary_crossentropy')
my_model.fit(x,y,batch_size=1,epochs=1000)

model_yaml = my_model.to_yaml()
with open('Machine_learning/Deep_learning/Save_model_DL/YAML_model/my_model_save.yaml','w') as yaml_file:
    yaml_file.write(model_yaml)
my_model.save_weights('Machine_learning/Deep_learning/Save_model_DL/YAML_model/my_model_Weight.tx')
print(my_model.predict_proba(x))