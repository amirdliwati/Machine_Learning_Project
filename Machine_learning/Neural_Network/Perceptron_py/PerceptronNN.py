## perceptron AND Neural Network

#  X1  	 X2  	 Y
#  –1	 –1 	–1
#  –1	  1   	–1
#   1	 -1  	–1
#   1	  1   	 1

import numpy as np


x = np.array([[1,1,-1,-1],[1,-1,1,-1]])
t = np.array([1,-1,-1,-1])
w = np.array([0,0])
b = 0 ## bias
alpha = int(input('Enter Learning rate=')) ## معامل التعلم
theta = int(input('Enter Threshold value=')) ## شرط تابع التفعيل 
# alpha = 1
# theta = 0
con = 1 ## شرط التوقف
epoch = 0 ## التكرار

while con :
    con = 0
    for i in range(4):
        yin = b + x[0,i] * w[0] + x[1,i] * w[1]
        if yin > theta :
            y = 1
        if yin <= theta & yin >= -theta :
            y = 0
        if yin<-theta :
            y = -1
        if y-t[i] :
            con = 1
            for j in range(2):
                w[j] = w[j] + alpha * t[i]* x[j,i]
            b = b + alpha * t[i]
    epoch = epoch + 1


print('Perceptron for AND funtion')
print(' Final Weight matrix')
print(w)
print('Final Bias')
print(b)
print('Final Epoch')
print(epoch)



###########   Test
# newW = np.array([1,1])
newW = w
newX = np.array([[-1,1,-1,1],[-1,-1,1,1]])
newB = b

for i in range(4):
    y_in = newB + newX[0,i] * newW[0] + newX[1,i] * newW[1]
    if y_in > theta :
        print('true y = 1 :  ',i)
    if y_in <= theta & yin >= -theta :
        print('y = 0 : ',i)
    if y_in<-theta :
        print('y = -1 :  ',i)
