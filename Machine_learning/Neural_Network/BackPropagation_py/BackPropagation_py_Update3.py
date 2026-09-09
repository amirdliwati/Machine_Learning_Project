## Back Propagation Network for XOR function with Binary Input and Output

#  X1  	 X2  	Y
#   0	  0 	0
#   0	  1   	1
#   1	  0  	1
#   1	  1   	0


import numpy as np

def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y

def derivative(x):
    y2 = sigmoid(x)*(1-sigmoid(x))
    return y2



## Initialize weights and bias
v = np.array([[0.197 ,0.3191 ,-0.1448 ,0.3394],[0.3099 ,0.1904 ,-0.0347 ,-0.4861]])
v1 = np.zeros([2,4])

b1 = np.array([-0.3378 ,0.2771 ,0.2859 ,-0.3329])
b2 = -0.1401

w = np.array([0.4919,-0.2913,-0.3979,0.3581])
w1 = np.zeros(4)

x = np.array([[1,1,0,0],[1,0,1,0]])
t = np.array([0,1,1,0])

alpha = 0.02
mf = 0.9
con = 1
epoch = 0
eps = 1e-8
rm = 0.999

while con:
    e = 0
    y = np.zeros(4)
    for I in range(4): ## عدد العينات
        
        ## Feed forward
        
        zin = np.zeros(4)
        z = np.zeros(4)

        for j in range(4):
            zin[j] = b1[j]
            for i in range(2):
                zin[j] = zin[j] + x[i,I] * v[i,j]
        
            z[j]=sigmoid(zin[j])
        
        yin = 0
        g = z*w
        for i in range(4):
            yin = yin + g[i]
        yin = yin + b2
        y[I] = sigmoid(yin)
        
        ##Backpropagation of Error
        
        delk = (t[I]-y[I])*derivative(yin)

        delinj = delk * w
        delj = np.zeros(4)
        for j in range(4):  ##   ديلتا المثلث
            delj[j] = delinj[j] * derivative(zin[j]) ## مصفوفة المثلثات

        ## Weight updation

        delv = np.zeros([2,4])
        for j in range(4):
            for i in range(2):
                delv[i,j] = alpha * delj[j] * x[i,I] + mf * (v[i,j] - v1[i,j]) ## Momentum  mf * (v[i,j] - v1[i,j])
        delb1 = alpha * delj

        delw = alpha * delk * z  + mf * (w-w1) ## Momentum mf*(w-w1)
        delb2 = alpha * delk

        w1 = w
        v1 = v      
        
        v = v+delv  ##  مصفوفة الأوزان الجديدة الطبقة الخفية
        b1 = b1+delb1  ## البياز الجديد الطبقة الخفية

        w = w+delw        ## مصفوفة الأوزان طبقة الخرج
        b2 = b2+delb2      ## البياز الجديد للطبقة الخرج


        e = e + (t[I]-y[I])**2 ## gradient Descent
    
    if e<0.005 :
        con=0
    
    epoch = epoch + 1
    if epoch==10000:
        print(epoch)
        print(e)
    # if epoch == 1:
    #     print('BPN for XOR funtion with Binary input and Output')
    #     print('\nTotal Epoch Performed: ',epoch)
    #     print('\nError: ',e)
    #     print('\nFinal Weight matrix V: \n',v)
    #     print('\nbias 1: ',b1)
    #     print('\nFinal Weight matrix W: \n',w)
    #     print('\nbias 2: ',b2)
    ###########################################################################
    # print(e)
    # if epoch == 5387:
    #     con=0

print('BPN for XOR funtion with Binary input and Output')
print('\nTotal Epoch Performed: ',epoch)
print('\nError: ',e)
print('\nFinal Weight matrix V: \n',v)
print('\nbias 1: ',b1)
print('\nFinal Weight matrix W: \n',w)
print('\nbias 2: ',b2)


###########   Test Predict
y = np.zeros(4)
for I in range(4): ## عدد العينات
        
        ## Feed forward
        zin = np.zeros(4)
        z = np.zeros(4)

        for j in range(4):
            zin[j] = b1[j]
            for i in range(2):
                zin[j] =  x[i,I] * v[i,j] + zin[j]
        
            z[j]=sigmoid(zin[j])
        
        yin = 0 
        g = z*w
        for i in range(4):
            yin = yin + g[i]
        yin = yin + b2
        y[I] = sigmoid(yin)

print('\n\nFinal predict: \n',y)