import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import LogisticRegression as lr
import math
import time

dataset = pd.read_csv('data.csv', sep=',', header=None)
arr = np.array(dataset)
size = np.size(arr,1)
x = np.asarray(arr[:,0:size-1])
y = np.asarray(arr[:,size-1])
no_of_iterations = 150001

alpha = 0.001
theta = np.array([-1.28, 0.02,0.01])

posx1= np.array([])
posx2= np.array([])
negx1= np.array([])
negx2= np.array([])

for i in range(x.__len__()):
    if y[i]==1:
        posx1 = np.append(posx1,x[i,0])
        posx2 = np.append(posx2,x[i,1])
    else:
        negx1 = np.append(negx1,x[i,0])
        negx2 = np.append(negx2,x[i,1])

logistic_regression = lr.LogisticRegression(theta, x, y, alpha)
iterations = np.array([])
costs = np.array([])
X = logistic_regression.get_x()
plot_x = [np.amin(X[:,1])-10,  np.amax(X[:,1])+10]
line_x = plot_x
line_y = [np.amin(X[:,2])-10,  np.amax(X[:,2])+10]

cnt = 0
for i in range(no_of_iterations):
    logistic_regression.gradient_decent()
    iterations = np.append(iterations,i)
    costs = np.append(costs,logistic_regression.cost())
    if i % 5000 == 0:
        #print("logistic_regression.get_theta() " , logistic_regression.get_theta())
        #\print("logistic_regression.cost() ", logistic_regression.cost())
        plt.clf()
        plt.scatter(posx1, posx2, color = 'b')
        plt.scatter(negx1, negx2, color = 'g')
        plt.xlabel('Feature1')
        plt.ylabel('Feature2')
        plt.xlim(line_x)
        plt.ylim(line_y)
        Theta = logistic_regression.get_theta()
        plot_y = (-1/Theta[2]) * (Theta[1] * plot_x + Theta[0]);
        plt.plot(plot_x, plot_y)
        plt.grid()
        tempString = 'image' + str(cnt)+'.png'
        plt.savefig(tempString)
        cnt = cnt + 1

print("logistic_regression.get_theta() " , logistic_regression.get_theta())
print("logistic_regression.cost() ", logistic_regression.cost())
plt.close()

cnt = 0

for i in range(no_of_iterations):
    if i % 5000 == 0:
        plt.clf()
        plt.scatter(iterations[i],costs[i],color="#00e600")
        plt.plot(iterations, costs,color = "#0099cc")
        plt.xlim(0,no_of_iterations-1)
        plt.xlabel('Iterations')
        plt.ylabel('Cost')
        plt.grid()
        tempString = 'cost' + str(cnt)+'.png'
        plt.savefig(tempString)
        cnt = cnt + 1
