import numpy as np

#5.6函数
def func_6_(x):
    return 0.5*(10*x[0]**2-18*x[0]*x[1]+10*x[1]**2)+4*x[0]-15*x[1]+13
def gfunc_6_(x):
    return np.array([10*x[0]-9*x[1]+4,
                     10*x[1]-9*x[0]-15])
def hess_6_(x):
    return np.array([[10,-9],[-9,10]])






