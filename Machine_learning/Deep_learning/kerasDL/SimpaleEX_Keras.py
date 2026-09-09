##   keras deep learning
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras import backend as k
from keras.utils.vis_utils import plot_model

my_model = Sequential()

# my_model.add(Dense(10,input_shape=(4,),activation = 'tanh'))
# my_model.add(Dense(8,activation='tanh'))
# my_model.add(Dense(6,activation='tanh'))
# my_model.add(Dense(3,activation='softmax'))

my_model.add(Dense(10,input_dim=4,activation = k.tanh))
my_model.add(Dense(8,activation=k.tanh))
my_model.add(Dense(6,activation=k.tanh))
my_model.add(Dense(3,activation=k.softmax))

my_model.compile(SGD(lr=0.1),loss='categorical_crossentropy',metrics=['accuracy'])
my_model.summary()

plot_model(my_model,to_file='Machine_learning/Deep_learning/kerasDL/plotDL.png',show_shapes=True,show_layer_names=True)
