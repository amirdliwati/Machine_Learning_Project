
"""         n        - Number of training examples.
        i        - ith training example in a data set.
        y(i)     - Ground truth label for ith training example.
        y_hat(i) - Prediction for ith training example. """



## Mean Square Error/Quadratic Loss/L2 Loss

## As the name suggests, Mean square error is measured as the average of squared 
# difference between predictions and actual observations. It’s only concerned with 
# the average magnitude of error irrespective of their direction. However, due to squaring, 
# predictions which are far away from actual values are penalized heavily in comparison to less 
# deviated predictions. Plus MSE has nice mathematical properties which makes it easier to calculate 
# radients.

import numpy as np

y_hat = np.array([0.000, 0.166, 0.333])
y_true = np.array([0.000, 0.254, 0.998])

def rmse(predictions, targets):
    differences = predictions - targets
    differences_squared = differences ** 2
    mean_of_differences_squared = differences_squared.mean()
    rmse_val = np.sqrt(mean_of_differences_squared)
    return rmse_val

print("d is: " + str(["%.8f" % elem for elem in y_hat]))
print("p is: " + str(["%.8f" % elem for elem in y_true]))

rmse_val = rmse(y_hat, y_true)
print("rms error is: " + str(rmse_val))

## Mean Absolute Error/L1 Loss

## Mean absolute error, on the other hand, is measured as the average of sum of absolute differences between predictions and actual observations.
#  Like MSE, this as well measures the magnitude of error without considering their direction.
#  Unlike MSE, MAE needs more complicated tools such as linear programming to compute the gradients.
#  Plus MAE is more robust to outliers since it does not make use of square.


import numpy as np

y_hat = np.array([0.000, 0.166, 0.333])
y_true = np.array([0.000, 0.254, 0.998])

print("d is: " + str(["%.8f" % elem for elem in y_hat]))
print("p is: " + str(["%.8f" % elem for elem in y_true]))

def mae(predictions, targets):
    differences = predictions - targets
    absolute_differences = np.absolute(differences)
    mean_absolute_differences = absolute_differences.mean()
    return mean_absolute_differences

mae_val = mae(y_hat, y_true)
print ("mae error is: " + str(mae_val))



## Mean Bias Error

## This is much less common in machine learning domain as compared to it’s counterpart.
#  This is same as MSE with the only difference that we don’t take absolute values.
#  Clearly there’s a need for caution as positive and negative errors could cancel each other out.
#  Although less accurate in practice, it could determine if the model has positive bias or negative bias.


