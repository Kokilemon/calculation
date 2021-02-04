import matplotlib.pyplot as plt
import numpy as np


def integrate(
    func, a=0, b=1, dx=1 / 100
):  # a < x < b, integrate func and return answer list
    x = np.arange(a, b, dx)
    fmem = np.zeros(len(x))
    f = 0
    for i in range(len(x)):
        f += func(x[i]) * dx
        fmem[i] = f
    return x, fmem


if __name__ == "__main__":

    def func(x):
        return np.sin(x)

    xx, yy = integrate(func, a=0, b=3 * np.pi, dx=1 / 100)

    #    import plt_func
    #    plt_func.plt_func(func, a=0, b=3*np.pi, dx=/100)

    plt.plot(xx, yy)
    plt.show()
