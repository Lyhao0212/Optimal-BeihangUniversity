import numpy as np
import matplotlib.pyplot as plt


def GN27(y0,f,gf,hessian,t,fi):

    X1 = np.linspace(-0.015,0.01,125)
    X2 = np.linspace(250,600,350)
    x1, x2 = np.meshgrid(X1, X2)  # 给定的函数
    y1=x1/x2
    y2=1/(96.05*x1)-1
    plt.contour(x1, x2, f(t,[y1, y2],fi), 30)  # 画出函数的20条轮廓线
    imax = 1000
    W = np.zeros((2, imax))
    m=np.zeros(2)
    m[0]=1/(96.05*(y0[1]+1))
    m[1]=m[0]/y0[0]
    W[:, 0] = m
    i = 1
    y = y0 # 初始误差
    delta=1
    while i < imax and delta > 10**(-6):
        g = gf(t,y,fi)
        G = hessian(t,y)
        Gni=np.linalg.inv(G)
        p=-Gni.dot(g)
        y0 = y
        y[0]=y[0]+p[0]
        y[1]=y[1]+p[1]
        m[0]=1/(96.05*(y[1]+1))
        m[1]=m[0]/y[0]
        W[:,i]=m

        delta = sum((y-y0)** 2)
        i = i + 1

    print("迭代次数为:", i)
    W = W[:, 0:i]  # 记录迭代点
    print(W)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(W[0, :], W[1, :], 'g*', W[0, :], W[1, :])  # 画出迭代点收敛的轨迹
    plt.title("5.27图")
    plt.show()
    return y






