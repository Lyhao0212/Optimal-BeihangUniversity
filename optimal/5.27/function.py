import numpy as np
#5.27函数

def fi_27_(t,y):
    return (1-t*y[0])**y[1]

def func_27_(t,y,fi):
    sum=0
    for i in range(len(t)):
        sum+=((1-t[i]*y[0])**y[1]-fi[i])**2
    return 0.5*sum

def gfunc_27_(t,y,fi):
    sum=[0,0]
    for i in range(len(t)):
        sum[0]+=(fi_27_(t[i],y)-fi[i])*\
             -1*t[i]*y[1]*(1-t[i]*y[0])**(y[1]-1)
        sum[1]+=(fi_27_(t[i],y)-fi[i])*\
             (1-t[i]*y[0])**y[1]*np.log(1-t[i]*y[0])

    return np.reshape(np.array(sum),(2,1))

def hess_27_(t,y):
    sum=np.zeros((6,2))
    j=0
    for i in range(len(t)):
        i = np.array([-1 * t[i] * y[1] * (1 - t[i] * y[0]) ** (y[1] - 1),(1-t[i]*y[0])**y[1]*np.log(1-t[i]*y[0])])
        sum[j,:]=i
        j = j + 1
    sum=np.dot(sum.T,sum)
    return  sum

