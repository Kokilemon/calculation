import matplotlib.pyplot as plt
import numpy as np

import integrate

if __name__ == "__main__":

    def func(x):
        return -(2 / np.pi * np.arcsin(2 * x) - 1) * 2

    xx, yy = integrate.integrate(func, a=0, b=1 / 2, dx=1 / 100)
    answer = yy[-1]

    print(yy[-1])
    print(2 / np.pi)

    plt.plot(xx, yy)

    plt.show()
