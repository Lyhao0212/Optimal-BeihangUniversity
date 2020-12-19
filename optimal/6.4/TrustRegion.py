from Steihaug import Steihaug
import numpy as np
from function import subqx

def TR(x0,n,f,g,hess):

    delta=2
    i=0
    norm=1
    while( norm>10**(-6)):

        gf=g(x0,n)
        G=hess(x0,n)
        norm=np.sqrt(np.dot(gf.T,gf))
        i = i + 1
        print("第",i,"次迭代：")
        s=Steihaug(G,gf,delta,n).reshape((2*n,1))
        norms=np.sqrt(np.dot(s.T,s))
        x=x0+s
        rho=(f(x,n)-f(x0,n))/subqx(s,G,gf)

        if rho<0.25:
            delta=delta/4
        elif rho>0.75 and np.abs(norms-delta)<10**(-2):
            delta=2*delta
        if rho > 0:
            x0 = x
        print("迭代之后的x值是：\n",x,'\n')
