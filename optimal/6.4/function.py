import numpy as np


#6.4题函数
def func_4_(x,n):
    sum=0
    for i in range(n):
        sum+=(1-x[2*i])**2+10*(x[2*i+1]-x[2*i]**2)**2
    return sum

def gfunc_4_(x,n):
    gf=np.zeros(2*n)
    i=0
    while(i<2*n):
        gf[i]=-2*(1-x[i])-40*x[i]*(x[i+1]-x[i]**2)
        gf[i+1]=20*(x[i+1]-x[i]**2)
        i=i+2
    return gf.reshape((2*n,1))

def hess_4_(x,n):
    G=np.zeros((2*n,2*n))
    i=0
    while(i<2*n):
        G[i,i]=2-40*x[i+1]+120*x[i]**2
        G[i,i+1]=-40*x[i]
        G[i+1,i]=-40*x[i]
        G[i+1,i+1]=20

        i=i+2
    return G

'''
def subq_4_(x0,f,g,G,n,s):
    return f(x0,n)+np.dot(g(x0,n).T,s)+0.5*np.dot(np.dot(s.T,G(x0,n)),s)
'''
#f（x0，n）为常数，所以上下两个函数做优化效果相同；
# 但上面子问题函数在调用时还需额外计算f（x0，n），降低迭代速度；
#故修改子问题函数形式，需要注意此时rho形式也做出相应改变
def subqx(x,G,g):
    return np.dot(x.T,np.dot(G,x))*0.5+np.dot(g.T,x)