import numpy as np
import matplotlib.pyplot as plt


#不带线搜索的一维牛顿法，用于5.7
def Newton7(x0,f,gf,hessian):
    X1 = np.arange(7, 9, 0.01)
    Y1=9*X1-4*np.log(X1-7)
    plt.plot(X1,Y1)
    print('初始点为:')
    print(x0, '\n')
    imax = 6
    X=np.zeros(imax)
    Y=np.zeros(imax)
    X[0]=x0
    Y[0]=f(x0)
    i = 1
    x = x0

    while i < imax:
        g = gf(x)
        G = hessian(x)
        p = -np.dot(g, 1/G)
        x = x +p
        X[i] = x
        Y[i]=f(x)
        i = i + 1

    print("迭代次数为:", i - 1)
    print("迭代结果为:")
    print(x, '\n') # 记录迭代点
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(X,Y,'r-')
    plt.scatter(X,Y,marker='o')
    plt.title("5.7图")
    plt.show()
