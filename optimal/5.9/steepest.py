import numpy as np
import matplotlib.pyplot as plt
from linesearch import armijosearch


#回溯线搜索最速下降法，用于5.9
def steepest(x0,f,gf):

    X1 = np.arange(-10, 10, 0.5)
    X2 = np.arange(-10, 10, 0.05)
    [x1, x2] = np.meshgrid(X1, X2)
    plt.contour(x1, x2, f([x1,x2]), 20)

    print('初始点为:')
    print(x0, '\n')
    imax = 20000
    W = np.zeros((2, imax))
    W[:, 0] = x0
    i = 0
    x = x0
    grad = gf(x)
    delta = sum(grad ** 2)  # 初始误差

    while i < imax and delta > 10 ** (-5):
        p = -gf(x)
        rho = armijosearch(f, gf, p, x, 0.1,0.5)
        x = x + rho * p
        W[:, i] = x
        grad = gf(x)
        delta = sum(grad ** 2)
        i = i + 1
        print("第",i,"迭代的步长为：",rho)

    print("迭代次数为:", i)
    print("近似最优解为:")
    print(x, '\n')
    W = W[:, 0:i]
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(W[0, :], W[1, :], 'g*', W[0, :], W[1, :])  # 画出迭代点收敛的轨迹
    plt.title("5.9最速下降法图")
    plt.show()