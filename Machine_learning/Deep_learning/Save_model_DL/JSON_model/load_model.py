##   keras deep learning XOR
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense
from keras.optimizers import SGD
from keras import backend as k
from keras.utils.vis_utils import plot_model
import numpy as np
import pickle as pl

x = np.array([[0,0],[1,0],[0,1],[1,1]])
y = np.array([[0],[1],[1],[0]])

json_file = open('Machine_learning/Deep_learning/Save_model_DL/JASON_model/my_model_save.json','r')
loaded_model_json = json_file.read()
json_file.close()
model_json = model_from_json(loaded_model_json)

model_json.load_weights('Machine_learning/Deep_learning/Save_model_DL/JASON_model/my_model_Weight.tx')

model_json.compile(SGD(lr=0.1),loss='binary_crossentropy')
print(model_json.predict_proba(x))