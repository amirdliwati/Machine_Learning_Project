import matplotlib.pyplot as plt
import numpy as np

""" My_list1 = [1,2,8,4,5,6]
plt.plot(My_list1)
plt.show() """

# plt.style.use('ggplot')

# My_list1 = [1,2,3,4,5,6] 
# My_list2 = [1,4,9,16,0,30]

# plt.plot(My_list1,My_list2)

# plt.xlabel("محور الأكسات")
# plt.ylabel("محور الوايات")

# plt.show()

""" x = np.arange(0,10,0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

plt.plot(x,y)

plt.xlim(0,10)
plt.ylim(-1,1)

plt.show() """

# x = np.arange(0.,10,0.1)
# a = np.cos(x)
# b = np.sin(x)
# c = np.exp(x/10)
# d = np.exp(-x/10)

# plt.plot(x,a,"b-",label = 'Cosin')
# plt.plot(x,b,"r--",label = "sin")
# plt.plot(x,c,"g-",label = "exp(+x)")
# plt.plot(x,d,"y-",linewidth = 5, label = "exp(-x)")

# plt.legend(loc='upeerleft')
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")

# plt.show()

n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)

plt.scatter(x,y)

plt.show()
