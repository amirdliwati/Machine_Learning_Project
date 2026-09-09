#!/usr/bin/env python
# coding: utf-8

# In[27]:


# create sigmoid Activation Function

def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y

def derivative(x):
    y2 = sigmoid(x)*(1-sigmoid(x))

    return y2


# In[28]:


## Initialize weights and bias and parametrs

import numpy as np
import math

v = np.array([[0.1975 ,0.3191 ,0.1448 ,0.3394],[0.3099 ,0.1904 ,0.0347 ,0.4861]])
v1 = np.zeros([2,4])

b1 = np.array([0.3378 ,0.2771 ,0.2859 ,0.3329])
b11 = np.zeros(4)
b2 = 0.1401
b22 = 0

w = np.array([0.4919,0.2913,0.3979,0.3581])
w1 = np.zeros(4)

x = np.array([[1,1,0,0],[1,0,1,0]])
t = np.array([0,1,1,0])

rm = 0.999 #RMSprop   0.999
mf = 0.9  #momentum  0.9
con = 1
epoch = 0
eps = 1e-8
#alpha = 10
alpha = 0.001


# In[29]:


# BackPropagation Algorithm

while con:
    e = 0.0
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
        delv1 = np.zeros([2,4])
        delvadam = np.zeros([2,4])
        for j in range(4):
            tt = j+1
            for i in range(2):
                delv[i,j] = mf * delj[j] * x[i,I] + ((1-mf) * (v[i,j] - v1[i,j])) ## Momentum  mf * (v[i,j] - v1[i,j])
                print(delv[i,j])
                print(delj[j])
                print(x[i,I])
                #delv1[i,j] = rm * delj[j] * x[i,I] + ((1-rm) * ((v[i,j] - v1[i,j])**2)) ## RMS
                #delv[i,j] =  delv[i,j] / (1-(mf**(tt)))
                #delv1[i,j] =  delv1[i,j] / (1-(rm**(tt)))
                #delvadam[i,j] = delv[i,j] / (math.sqrt(abs(delv1[i,j])+ eps))
        
        #delb1 = alpha * delj
        #delb1 = (mf * delj)
        delb1 = (mf * delj) + ((1-mf) * (b1 - b11))
        #delb11 = rm * delj + ((1-rm) * ((b1 - b11)**2))
        
        #delb1 = delb1 / (1-(mf**(tt)))
        #delb11 = delb11 / (1-(rm**(tt)))
        #delb1adam = np.zeros(4)
        #for ii in range(4):
            #delb1adam[ii] = delb1[ii] / (math.sqrt(abs(delb11[ii])+ eps))
        
        
        delw = mf * (delk * z)  + ((1-mf) * (w-w1)) ## Momentum mf*(w-w1)
        #delw1 = rm * delk * z  + ((1-rm) * ((w-w1)**2)) ## RMS
        #delw = delw / (1-(mf**(tt)))
        #delw1 =  delw1 / (1-(rm**(tt)))
        #delwadam = np.zeros(4)
        #for ii in range(4):
            #delwadam[ii] = delw[ii] / (math.sqrt(abs(delw1[ii])+ eps))
        
        #delb2 = alpha * delk
        #delb2 = (mf * delk)
        delb2 = (mf * delk) + ((1-mf) * (b2 - b22))
        #delb22 = rm * delk + ((1-rm) * ((b2 - b22)**2))

        #delb2 = delb2 / (1-(mf**(tt)))
        #delb22 = delb22 / (1-(rm**(tt)))
        #delb2adam = delb2 / (math.sqrt(abs(delb22)+ eps))
        
        
        w1 = w
        v1 = v      
        b11 = b1
        b22 = b2
        
        v = v - (alpha * delv)  ##  مصفوفة الأوزان الجديدة الطبقة الخفية
        b1 = b1 - (alpha * delb1)  ## البياز الجديد الطبقة الخفية

        w = w - (alpha * delw)       ## مصفوفة الأوزان طبقة الخرج
        b2 = b2 - (alpha * delb2)      ## البياز الجديد للطبقة الخرج


        e = e + (t[I]-y[I])**2 ## gradient Descent
    
    if e<0.005 :
        con=0
    
    epoch = epoch + 1
    if epoch==6000:
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


# In[ ]:


# OutPut
0.007034097126630948
-0.014128780970410053
1
print('BPN for XOR funtion with Binary input and Output')
print('\nTotal Epoch Performed: ',epoch)
print('\nError: ',e)
print('\nFinal Weight matrix V: \n',v)
print('\nbias 1: ',b1)
print('\nFinal Weight matrix W: \n',w)
print('\nbias 2: ',b2)


# In[295]:


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


# In[241]:


print(math.sqrt(1000))
print(1e-2 * 10)
print(10 /1000)
abs(-5)


# In[ ]:


import math

alpha = 0.01
beta_1 = 0.9
beta_2 = 0.999						#initialize the values of the parameters
epsilon = 1e-8
def func(x):
	return x*x -4*x + 4
def grad_func(x):					#calculates the gradient
	return 2*x - 4
theta_0 = 0						#initialize the vector
m_t = 0 
v_t = 0 
t = 0

while (1):					#till it gets converged
	t+=1
	g_t = grad_func(theta_0)		#computes the gradient of the stochastic function
	m_t = beta_1*m_t + (1-beta_1)*g_t	#updates the moving averages of the gradient
	v_t = beta_2*v_t + (1-beta_2)*(g_t*g_t)	#updates the moving averages of the squared gradient
	m_cap = m_t/(1-(beta_1**t))		#calculates the bias-corrected estimates
	v_cap = v_t/(1-(beta_2**t))		#calculates the bias-corrected estimates
	theta_0_prev = theta_0								
	theta_0 = theta_0 - (alpha*m_cap)/(math.sqrt(v_cap)+epsilon)	#updates the parameters
	if(theta_0 == theta_0_prev):		#checks if it is converged or not
		break


# In[239]:



import numpy as np 
#np.random.seed(0)

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

#Input datasets
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
expected_output = np.array([[0],[1],[1],[0]])

epochs = 10000
lr = 0.1
inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2,2,1

#Random weights and bias initialization
hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
hidden_bias =np.random.uniform(size=(1,hiddenLayerNeurons))
output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
output_bias = np.random.uniform(size=(1,outputLayerNeurons))

print("Initial hidden weights: ",end='')
print(*hidden_weights)
print("Initial hidden biases: ",end='')
print(*hidden_bias)
print("Initial output weights: ",end='')
print(*output_weights)
print("Initial output biases: ",end='')
print(*output_bias)


#Training algorithm
for _ in range(epochs):
	#Forward Propagation
	hidden_layer_activation = np.dot(inputs,hidden_weights)
	hidden_layer_activation += hidden_bias
	hidden_layer_output = sigmoid(hidden_layer_activation)

	output_layer_activation = np.dot(hidden_layer_output,output_weights)
	output_layer_activation += output_bias
	predicted_output = sigmoid(output_layer_activation)

	#Backpropagation
	error = expected_output - predicted_output
	d_predicted_output = error * sigmoid_derivative(predicted_output)
	
	error_hidden_layer = d_predicted_output.dot(output_weights.T)
	d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

	#Updating Weights and Biases
	output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
	output_bias += np.sum(d_predicted_output,axis=0,keepdims=True) * lr
	hidden_weights += inputs.T.dot(d_hidden_layer) * lr
	hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True) * lr

print("Final hidden weights: ",end='')
print(*hidden_weights)
print("Final hidden bias: ",end='')
print(*hidden_bias)
print("Final output weights: ",end='')
print(*output_weights)
print("Final output bias: ",end='')
print(*output_bias)

print("\nOutput from neural network after 10,000 epochs: ",end='')
print(*predicted_output)


# In[308]:


5-10*2


# In[4]:


x = 0.9 * (0.55 * 3)
print(x)


# In[ ]:




