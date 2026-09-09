##UnSupervised  PCA Principal Component Analysis
import numpy as np
import matplotlib.pyplot as matplot
from sklearn.decomposition import PCA
from matplotlib import style

style.use('ggplot')

rng = np.random.RandomState(1)
my_input = np.dot(rng.rand(2,2),rng.randn(2,100)).T


my_model = PCA(n_components=1)
my_model.fit(my_input)

my_input_pca = my_model.transform(my_input)

print('The Orginal shape : ',my_input.shape)
print('The transform shape :',my_input_pca.shape)

my_input_newalues = my_model.inverse_transform(my_input_pca)
matplot.scatter(my_input[:,0],my_input[:,1])
matplot.scatter(my_input_newalues[:,0],my_input_newalues[:,1])
matplot.show()