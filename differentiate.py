import matplotlib.pyplot as plt
import numpy as np


def differentiate(func, a=0, b=1, dx=1 / 100):
    x = np.arange(a, b, dx)
    df = np.zeros(len(x))
    for i in range(len(x) - 1):
        df[i] = (func(x[i + 1]) - func(x[i])) / dx
    return x, df


if __name__ == "__main__":

    def func(x):
        return np.sin(x)

    xx, yy = differentiate(func, a=0, b=3 * np.pi, dx=1 / 100)

    #    import plt_func
    #    plt_func.plt_func(func, a=0, b=3*np.pi, dx=1/100)

    plt.plot(xx, yy)

    plt.show()
