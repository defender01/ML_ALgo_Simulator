import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PolynomialFitting import LinearRegression as lr
import time

class Visualization:

    def call_simulation(self):
        dataset = pd.read_csv('D:\webDevelopment\Ml_Algo_Simulator\PolynomialFitting\data.csv', sep=',', header = None)
        arr = np.array(dataset)
        size = np.size(arr,1)
        x = np.asarray(arr[:,0:size-1])
        y = np.asarray(arr[:,size-1])

        alpha = 0.01
        theta = np.array([0.0, 0.0, 0.0])

        linear_regression = lr.LinearRegression(theta, x, y, alpha)
        linear_regression.feature_normalize()

        iterations = np.array([])
        costs = np.array([])
        X = linear_regression.get_x()
        Y = linear_regression.get_y()
        plot_x = [np.amin(X[:,1])-10,  np.amax(X[:,1])+10]
        plot_y = [np.amin(Y)-10,  np.amax(Y)+10]

        cnt = 0

        for i in range(1501):
            linear_regression.gradient_decent()
            iterations = np.append(iterations,i)
            costs = np.append(costs,linear_regression.cost())
            if i % 50 == 0:
                plt.clf()
                plt.xlabel('Feature')
                plt.scatter(linear_regression.get_x()[:, 1], linear_regression.get_y(), color='k', marker='x')
                plt.ylabel('Output')
                plt.xlim(plot_x)
                plt.ylim(plot_y)
                plt.grid()

                x_list = np.arange(plot_x[0],plot_x[1])
                x_list_reshaped = np.reshape(x_list,(-1,1))

                plt.plot(x_list, linear_regression.predict_with_feature_scaling(x_list_reshaped))
                tempString = 'D:\webDevelopment\Ml_Algo_Simulator\PolynomialFitting\image' + str(cnt)+'.png'
                plt.savefig(tempString)
                cnt = cnt + 1

        print(linear_regression.get_theta())
        print(linear_regression.cost())
        plt.close()

        cnt = 0
        for i in range(1501):
            if i % 50 == 0:
                plt.clf()
                plt.scatter(iterations[i],costs[i],color="#00e600")
                plt.plot(iterations, costs,color = "#0099cc")
                plt.xlim(0,1500)
                plt.xlabel('Iterations')
                plt.ylabel('Cost')
                plt.grid()
                tempString = 'D:\webDevelopment\Ml_Algo_Simulator\PolynomialFitting\cost' + str(cnt)+'.png'
                plt.savefig(tempString)
                cnt = cnt + 1
