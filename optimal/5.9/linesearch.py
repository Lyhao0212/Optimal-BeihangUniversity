
import numpy as np

def armijosearch(f, df, d, x,rho,sigma):
    m = 0
    mk=0
    a = 0
    fk = f(x)
    gk = df(x)
    '''
    x0时的f和f‘
    '''
    phi0 = fk
    dphi0 = np.dot(gk, d)
    while (m<20):
        newfk = f(x + rho**m * d)

        phi = newfk
        '''
        新的函数值
        '''
        if (phi - phi0 <= sigma*rho** m * dphi0):
                mk=m
                break
        m=m+1;
    rhok=rho**mk
    return rhok


