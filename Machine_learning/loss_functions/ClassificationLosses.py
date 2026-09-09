""" 
        n        - Number of training examples.
        i        - ith training example in a data set.
        y(i)     - Ground truth label for ith training example.
        y_hat(i) - Prediction for ith training example. """



## Hinge Loss/Multi class SVM Loss

## In simple terms, the score of correct category should be greater than sum of scores of all incorrect
#  categories by some safety margin (usually one). And hence hinge loss is used for maximum-margin
#  classification, most notably for support vector machines. Although not differentiable,
#  it’s a convex function which makes it easy to work with usual convex optimizers used in machine learning
#  domain.

## Consider an example where we have three training examples and three classes to predict — Dog, cat and horse.
#  Below the values predicted by our algorithm for each of the classes :-

## Computing hinge losses for all 3 training examples :-

## 1st training example
""" max(0, (1.49) - (-0.39) + 1) + max(0, (4.21) - (-0.39) + 1)
max(0, 2.88) + max(0, 5.6)
2.88 + 5.6
8.48 (High loss as very wrong prediction) """

## 2nd training example
""" max(0, (-4.61) - (3.28)+ 1) + max(0, (1.46) - (3.28)+ 1)
max(0, -6.89) + max(0, -0.82)
0 + 0
0 (Zero loss as correct prediction) """

## 3rd training example
""" max(0, (1.03) - (-2.27)+ 1) + max(0, (-2.37) - (-2.27)+ 1)
max(0, 4.3) + max(0, 0.9)
4.3 + 0.9
5.2 (High loss as very wrong prediction)
 """

##  Cross Entropy Loss/Negative Log Likelihood

## This is the most common setting for classification problems.
#  Cross-entropy loss increases as the predicted probability diverges from the actual label.

## Notice that when actual label is 1 (y(i) = 1), second half of function disappears whereas in
#  case actual label is 0 (y(i) = 0) first half is dropped off. In short, we are just multiplying the log of the
#  actual predicted probability for the ground truth class. An important aspect of this is that
#  cross entropy loss penalizes heavily the predictions that are confident but wrong.

import numpy as np

predictions = np.array([[0.25,0.25,0.25,0.25],
                        [0.01,0.01,0.01,0.96]])
targets = np.array([[0,0,0,1],
                   [0,0,0,1]])

def cross_entropy(predictions, targets, epsilon=1e-10):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce_loss = -np.sum(np.sum(targets * np.log(predictions + 1e-5)))/N
    return ce_loss

cross_entropy_loss = cross_entropy(predictions, targets)
print ("Cross entropy loss is: " + str(cross_entropy_loss))