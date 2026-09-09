##   keras deep learning XOR
import pickle as pl
import numpy as np

x = np.array([[0,0],[1,0],[0,1],[1,1]])
my_model = pl.load(open('Machine_learning/Deep_learning/kerasDL/Mymodel_save.txt','rb'))
print(my_model.predict_proba(x))