##UnSupervised  Kmeans أنا بعرف عدد الكلاستر أو فيني حدد عدد الكلاستر

import numpy as np
import matplotlib.pyplot as matplot
from sklearn.cluster import KMeans
from matplotlib import style

style.use('ggplot')

my_input = np.array([[4,2],[6,6],[2.6,4],[7,8],[3.5,5],[6,11]])

my_model = KMeans(n_clusters=2)
my_model.fit(my_input)

print('Cluster Centers : \n',my_model.cluster_centers_)
print('labels :',my_model.labels_)
colors = ['g.','r.','c.','y.']

matplot.scatter(my_input[:,0],my_input[:,1],c=my_model.labels_)
matplot.scatter(my_model.cluster_centers_[:,0],my_model.cluster_centers_[:,1],marker='x',linewidths=5)
matplot.show()