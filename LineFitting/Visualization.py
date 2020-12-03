import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from LineFitting import LinearRegression as lr
import time


class Visualization:

    def call_simulation(self):
        dataset = pd.read_csv('D:\webDevelopment\Ml_Algo_Simulator\LineFitting\data.csv', sep=',', header=None)
        arr = np.array(dataset)
        size = np.size(arr, 1)
        x = np.asarray(arr[:, 0:size - 1])
        y = np.asarray(arr[:, size - 1])
        print(x)

        alpha = 0.01
        theta = np.array([15.0, 1.0])

        linear_regression = lr.LinearRegression(theta, x, y, alpha)
        iterations = []
        costs = []
        X = linear_regression.get_x()
        Y = linear_regression.get_y()
        plot_x = [np.amin(X[:, 1]) - 5, np.amax(X[:, 1]) + 5]
        plot_y = [np.amin(Y) - 5, np.amax(Y) + 5]

        cnt = 0
        for i in range(3001):
            linear_regression.gradient_decent()
            iterations.append(i)
            costs.append(linear_regression.cost())
            if i % 100 == 0:
                plt.clf()
                plt.scatter(linear_regression.get_x()[:, 1], linear_regression.get_y(), color='k', marker='x')
                plt.xlabel('Feature')
                plt.ylabel('Output')
                plt.xlim(plot_x)
                plt.ylim(plot_y)
                plt.grid()
                line_x = np.reshape(plot_x, (-1, 1))
                line_y = linear_regression.predict(line_x)

                plt.plot(line_x, line_y)
                tempString = 'D:\webDevelopment\Ml_Algo_Simulator\LineFitting\image' + str(cnt) + '.png'
                plt.savefig(tempString)
                cnt = cnt + 1

        print(linear_regression.get_theta())
        print(linear_regression.cost())
        plt.close()

        cnt = 0

        for i in range(3001):
            if i % 100 == 0:
                plt.clf()
                plt.scatter(iterations[i], costs[i], color="#00e600")
                plt.plot(iterations, costs, color="#0099cc")
                plt.xlim(0, 3000)
                plt.xlabel('Iterations')
                plt.ylabel('Cost')
                plt.grid()
                tempString = 'D:\webDevelopment\Ml_Algo_Simulator\LineFitting\cost' + str(cnt) + '.png'
                plt.savefig(tempString)
                cnt = cnt + 1
