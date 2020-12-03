import numpy as np
import matplotlib.pyplot as plt
import time
import math

class gradientDescent:

    def deriv(self,x):
        x_deriv = 0.2 * x
        return x_deriv

    def simulation(self,x_new, precision, l_r):
        # file = open("Details.txt", "w"
        function = lambda x: (0.1 * (x ** 2))
        # Get 1000 evenly spaced numbers between -1 and 3 (arbitratil chosen to ensure steep curve)
        x = np.linspace(-60, 60, 500)

        idx = 0
        x_list = np.array([x_new])

        while True:

            idx = idx + 1

            x_prev = x_new

            d_x = self.deriv(x_prev)

            x_new = x_prev - (l_r * d_x)
            x_list = np.append(x_list, x_new)

            print("x_prev : " + str(x_prev) + " x_new : " + str(x_new))

            if abs(x_new - x_prev) < precision: break

        #file.write("Learning rate " + str(l_r) + "\n")
        #file.write("Number of iterations: " + str(i) + "\n")
        print("Number of iterations: " + str(idx))

        x_list = np.around(x_list, decimals=4)

        if(idx<=20): skip = 1
        else: skip = int(idx/20)

        cnt = 0
        for i in range(idx+1):
            if (i==0 or i%skip==0 or i==idx):
                plt.clf()
                x_new = x_list[i]
                plt.scatter(x_new, function(x_new), c="#00e600")
                plt.plot(x, function(x), c="#0099cc")
                plt.xlabel('x')
                plt.ylabel('y')
                plt.legend(['Function(x)', 'Current x'])
                plt.xlim([-60, 60])
                plt.ylim([-50, 400])
                plt.grid()
                #tempString = 'D:\webDevelopment\Ml_Algo_Simulator\GradientDescent\image' + str(idx) + '.png'
                tempString = 'D:\webDevelopment\Ml_Algo_Simulator\GradientDescent\image' + str(cnt) + '.png'
                plt.savefig(tempString)
                cnt = cnt + 1
        #for X in np.nditer(x_list):
        #   file.write("Current_x = " + str(X) + " d/dx = " + str(round(self.deriv(X), 4)) + "\n")

        #file.write("Local minimum occurs at: " + str(x_new) + "\n")
        print("Local minimum occurs at: " + str(x_new))

        # file.close()

        return cnt

    def call_simulation(self,startX,alpha):

        # initial_x = float(input("Enter the value of initial_x from where gradient descent will start : "))
        initial_x = startX

        return self.simulation(initial_x, 0.001, alpha)
