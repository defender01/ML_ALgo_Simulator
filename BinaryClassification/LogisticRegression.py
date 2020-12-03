import numpy as np
from scipy.special import expit
import math

class LogisticRegression:
    alpha = float(0)
    theta = np.array([0.0, 0.0])
    x = np.array([[0.0, 0.0], [0.0, 0.0]])
    y = np.array([0.0, 0.0])

    def __init__(self, _theta, _x, _y, _alpha):
        _x = np.append(np.ones((_x.__len__(), 1)), _x, axis=1)
        if _x.__len__() != _y.__len__():
            raise ValueError('Incompatible matrix size : x y')
        if _x.shape[1] != _theta.__len__():
            raise ValueError('Incompatible matrix size: x theta')
        self.theta = _theta
        self.theta = self.theta.reshape(-1,1)
        self.x = _x
        self.y = _y
        self.y = self.y.reshape(-1,1)
        self.alpha = float(_alpha)

    def sigmoid(self, _vector):
        _vector = np.array(_vector)
        _vector = _vector * (-1)
        _vector = np.exp(_vector)
        _vector = 1/(1 + _vector)
        return _vector

    def getPredictionVector_Xtheta(self):
        product = np.matmul(self.x,self.theta)
        product = self.sigmoid(product)
        product = product.reshape(-1,1)
        return product

    def predict(self, _x):
        _x = np.append(np.ones((_x.__len__(), 1)), _x, axis=1)
        _p = self.sigmoid(np.matmul(_x, self.theta))
        _p = (_p>=0.5)
        return _p

    def cost(self):
        m=self.y.__len__()
        H = self.getPredictionVector_Xtheta()
        if 0 in H or 1 in H:
            return float('inf')
        return (-1/m) * (np.matmul(np.transpose(self.y) , np.log(H)) + np.matmul(np.transpose((1-self.y)) , np.log( 1-H)))[0]

    def gradient_decent(self):
        m = self.y.__len__()
        errorVector = self.getPredictionVector_Xtheta() - self.y
        self.theta = self.theta - (self.alpha/m) * np.matmul(np.transpose(self.x) , errorVector)

    def get_theta(self):
        return self.theta

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_alpha(self):
        return self.alpha
