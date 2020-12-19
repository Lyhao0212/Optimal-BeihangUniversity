import numpy as np
import matplotlib.pyplot as plt
from linesearch import armijosearch_u


#函数带参数u的牛顿法，用于5.8

def NewtonNoLS(x0,f,gf,hessian,u):


    X1 = np.arange(0, 100 + 0.05, 0.5)
    X2 = np.arange(0, 100+ 0.05, 0.05)
    [x1, x2] = np.meshgrid(X1, X2)  # 给定的函数
    plt.contour(x1, x2, f([x1, x2],u), 20)  # 画出函数的20条轮廓线

    print('初始点为:')
    print(x0, '\n')
    imax = 1000
    W = np.zeros((2, imax))
    W[:, 0] = x0
    i = 1
    x = x0 # 初始误差
    delta=1

    while i < imax and delta > 10 ** (-5) and x[0]>0 and x[1]>0 and x[0]+x[1]<100 and x[0]-x[1]<50:
        g = gf(x,u)
        G = hessian(x,u)
        Gni=np.linalg.inv(G)
        p=-np.dot(g,Gni)
        x0 = x
        x=x+p
        W[:, i] = x
        delta = sum((x-x0)** 2)
        i = i + 1

    print("迭代次数为:", i-1)
    print("迭代结果为:")
    print(x, '\n')
    W = W[:, 0:i]  # 记录迭代点
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(W[0, :], W[1, :], 'g*', W[0, :], W[1, :])  # 画出迭代点收敛的轨迹
    plt.title("5.8图,不带线搜索")
    plt.show()


#函数带参数u的牛顿法，用于5.8
def NewtonLS(x0,f,gf,hessian,u):

    X1 = np.arange(0, 100 + 0.05, 0.5)
    X2 = np.arange(0, 100+ 0.05, 0.05)
    [x1, x2] = np.meshgrid(X1, X2)  # 给定的函数
    plt.contour(x1, x2, f([x1, x2],u), 20)  # 画出函数的20条轮廓线

    print('初始点为:')
    print(x0, '\n')
    imax = 1000
    W = np.zeros((2, imax))
    W[:, 0] = x0
    i = 1
    x = x0 # 初始误差
    delta=1

    while i < imax and delta > 10 ** (-5) and x[0]>0 and x[1]>0 and x[0]+x[1]<100 and x[0]-x[1]<50:
        g = gf(x,u)
        G = hessian(x,u)
        Gni=np.linalg.inv(G)
        p=-np.dot(g,Gni)
        x0 = x
        rho = armijosearch_u(f, gf,u, p, x, 0.6, 0.5)
        x = x + rho*p
        W[:, i] = x
        delta = sum((x-x0)** 2)
        i = i + 1

    print("迭代次数为:", i-1)
    print("迭代结果为:")
    print(x, '\n')
    W = W[:, 0:i]  # 记录迭代点
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(W[0, :], W[1, :], 'g*', W[0, :], W[1, :])  # 画出迭代点收敛的轨迹
    plt.title("5.8图,带线搜索")
    plt.show()



