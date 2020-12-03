import numpy as np

class LinearRegression:
    alpha = float(0)
    theta = np.array([0.0, 0.0,0.0])
    x = np.array([[0.0, 0.0,0.0], [0.0, 0.0,0.0]])
    y = np.array([0.0, 0.0])
    x_scaled = np.array([[0.0, 0.0,0.0], [0.0, 0.0,0.0]])
    mean = np.array([0.0])
    std  = np.array([0.0])

    def __init__(self, _theta, _x, _y, _alpha):
        _xsquare = _x ** 2;
        _x = np.append(np.ones((_x.__len__(), 1)), _x, axis=1)
        _x = np.append(_x,_xsquare,axis = 1)
        if _x.__len__() != _y.__len__():
            raise ValueError('Incompatible matrix size : x y')
        if _x.shape[1] != _theta.__len__():
            raise ValueError('Incompatible matrix size: x theta')
        self.theta = _theta
        self.theta = self.theta.reshape(-1,1)
        self.x = np.array(_x)
        self.x_scaled = np.array(_x)
        self.y = _y
        self.y = self.y.reshape(-1,1)
        self.alpha = float(_alpha)
        self.mean = np.zeros((1,_theta.__len__()))
        self.std = np.ones((1,_theta.__len__()))


    def getPredictionVector_Xtheta(self):
        product = np.matmul(self.x,self.theta)
        product = product.reshape(-1,1)
        return product

    def getPredictionVector_Xtheta_scaled(self):
        product = np.matmul(self.x_scaled,self.theta)
        product = product.reshape(-1,1)
        return product

    def predict(self, _x):
        _xsquare = (_x ** 2)
        _x = np.append(np.ones((_x.__len__(), 1)), _x, axis=1)
        _x = np.append(_x,_xsquare,axis = 1)
        return np.matmul(_x, self.theta)

    def predict_with_feature_scaling(self, _x):
        _xsquare = (_x ** 2)
        _x = np.append(np.ones((_x.__len__(), 1)), _x, axis=1)
        _x = np.append(_x,_xsquare,axis = 1)
        n = np.size(_x,1) - 1
        for i in range(n):
            _x[:,i+1] = _x[:,i+1] - self.mean[0,i+1]
            _x[:,i+1] = _x[:,i+1] / self.std[0,i+1]
        return np.matmul(_x, self.theta)

    def cost(self):
        m=self.y.__len__()
        #print("X :  -----")
        #print(self.x)
        #print("self.getPredictionVector_Xtheta() :")
        #print(self.getPredictionVector_Xtheta())
        errorVector = self.getPredictionVector_Xtheta_scaled() - self.y
        #print("errorVector : ")
        #print(errorVector)
        return (np.matmul(np.ones((1, m)), (errorVector**2))/(m*2))[0]

    def gradient_decent(self):
        m = self.y.__len__()
        errorVector = self.getPredictionVector_Xtheta_scaled() - self.y
        self.theta = self.theta - (self.alpha/m) * np.matmul(np.transpose(self.x_scaled) , errorVector)

    def feature_normalize(self):
        n = self.theta.__len__()-1
        for i in range(n):
            meani = np.mean(self.x[:,i+1])
            stdi  = np.std(self.x[:,i+1])

            self.x_scaled[:,i+1] = self.x_scaled[:,i+1] - meani
            self.x_scaled[:,i+1] = self.x_scaled[:,i+1] / stdi

            self.mean[0,i+1] = meani
            self.std[0,i+1]  = stdi

    def get_theta(self):
        return self.theta

    def get_x(self):
        return self.x

    def get_x_scaled(self):
        return self.x_scaled

    def get_y(self):
        return self.y

    def get_alpha(self):
        return self.alpha

    def get_mean(self):
        return self.mean

    def get_std(self):
        return self.std
