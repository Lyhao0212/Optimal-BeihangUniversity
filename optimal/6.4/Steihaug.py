import numpy as np
from function import subqx

def Steihaug(G,g,delta,n):
    i = 0
    epsilon=10**(-6)
    x=np.zeros(2*n).reshape((2*n,1))
    r=g
    p=-g
    normr=np.sqrt(np.dot(r.T,r))
    if normr<epsilon:
        print("子问题无需迭代，梯度为0")
        return np.zeros(2*n).reshape((2*n,1))
    else:
        while(1):
            i=i+1
            if(np.dot(p.T,np.dot(G,p))<=0):
                tau1=(-1*np.dot(p.T,x)+np.sqrt((np.dot(p.T,x))**2-np.dot(p.T,np.dot(p,(np.dot(x.T,x)-delta**2)))))/np.dot(p.T,p)
                tau2=(-1*np.dot(p.T,x)-np.sqrt((np.dot(p.T,x))**2-np.dot(p.T,np.dot(p,(np.dot(x.T,x)-delta**2)))))/np.dot(p.T,p)
                if(subqx(x+tau1,G,g)<subqx(x+tau1,G,g)):
                    x=x+tau1*p
                else:
                    x=x+tau2*p
                s=x
                print("子问题经过",i,"次迭代，遇到非正曲率停止迭代")
                return s
            alpha=np.dot(r.T,r)/np.dot(p.T,np.dot(G,p))
            x0=x
            x=x+alpha*p
            normx = np.sqrt(np.dot(x.T, x))
            if(normx>=delta):
                tau1 = (-1 * np.dot(p.T, x0) + np.sqrt(
                    (np.dot(p.T, x0)) ** 2 - np.dot(p.T, np.dot(p, (np.dot(x0.T, x0) - delta ** 2))))) / np.dot(p.T, p)
                tau2 = (-1 * np.dot(p.T, x0) - np.sqrt(
                    (np.dot(p.T, x0)) ** 2 - np.dot(p.T, np.dot(p, (np.dot(x0.T, x0) - delta ** 2))))) / np.dot(p.T, p)
                if (subqx(x0 + tau1, G, g) < subqx(x0 + tau1, G, g)):
                    x = x0 + tau1 * p
                else:
                    x = x0 + tau2 * p
                s = x
                print("子问题经过",i,"次迭代，达到信赖域边界停止迭代")
                return s
            r_old = r
            r = r + alpha * np.dot(G,p)
            normr=np.sqrt(np.dot(r.T,r))
            normr_old=np.sqrt(np.dot(r_old.T,r_old))
            if(normr<epsilon*normr_old):
                s=x
                print("子问题经过",i,"次迭代，满足停止条件停止迭代")
                return s
            beta=normr**2/normr_old**2
            p=-r+beta*p
    print("迭代次数为：",i)
    return s

