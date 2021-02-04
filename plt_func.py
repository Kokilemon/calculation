import matplotlib.pyplot as plt
import numpy as np


def plt_func(func, a=0, b=1, dx=1 / 100):
    xx = np.arange(a, b, dx)
    yy = np.zeros(len(xx))
    for i in range(len(xx)):
        yy[i] = func(xx[i])

    plt.plot(xx, yy)
    plt.show()
