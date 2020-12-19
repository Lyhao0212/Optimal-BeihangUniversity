import numpy as np

#5.9函数
def func_9_(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
def gfunc_9_(x):
    return np.array([-400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0]),
                     200 * (x[1] - x[0] ** 2)])
def hess_9_(x):
    return np.array([[1200*x[0]**2-400*x[1]+2,-400*x[0]],
                     [-400*x[0],200]])

