import numpy as np

def CreatHilbert(n):
    H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            H[i][j]=1.0/(i+1+j+1-1)

    return H
def Creatb(n):
    return np.ones(n).reshape(n,1)

def ConhugateGradient(x0,G,b):
    print('初始点为:')
    print(x0, '\n')
    i = 0
    x = x0
    delta = 1
    g2=g0=np.dot(G,x0)-b
    p2=-g0
    while(delta>10**(-6)):
        g1=g2
        p1=p2
        d=np.dot(G,p1)
        alph=float(np.dot(g1.T,g1)/np.dot(p1.T,d))
        x=x+alph*p1
        delta = np.dot(g1.T,g1)
        g2=g1+alph*d
        beta=np.dot(g2.T,g2)/np.dot(g1.T,g1)
        p2=-g2+beta*p1
        i=i+1

    print("最优解为：\n",np.linalg.inv(G).dot(b))

    print("迭代次数为:", i )
    print("近似最优解为:")
    print(x, '\n')


