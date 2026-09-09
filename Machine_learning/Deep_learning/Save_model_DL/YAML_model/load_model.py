##   keras deep learning XOR
from keras.models import Sequential
from keras.models import model_from_yaml
from keras.layers import Dense
from keras.optimizers import SGD
from keras import backend as k
from keras.utils.vis_utils import plot_model
import numpy as np
import pickle as pl

x = np.array([[0,0],[1,0],[0,1],[1,1]])
y = np.array([[0],[1],[1],[0]])

yaml_file = open('Machine_learning/Deep_learning/Save_model_DL/YAML_model/my_model_save.yaml','r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
model_yaml = model_from_yaml(loaded_model_yaml)

model_yaml.load_weights('Machine_learning/Deep_learning/Save_model_DL/YAML_model/my_model_Weight.tx')

model_yaml.compile(SGD(lr=0.1),loss='binary_crossentropy')
print(model_yaml.predict_proba(x))