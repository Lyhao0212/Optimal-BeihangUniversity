import numpy as np
from function import func_27_,gfunc_27_,hess_27_
from GNmethod import GN27
import warnings
warnings.filterwarnings("ignore")

print("-----5.27-----\n")


x=np.array([0.00333,333])
y=np.array([0.,0.])
y[0]=x[0]/x[1]
y[1]=1/(96.05*x[0])-1
print("初始点为：")
print(x,'\n')
t=np.array([2000,5000,10000,20000,30000,50000])
d=np.array([0.9427,0.8616,0.7384,0.5362,0.3739,0.3096])
y=GN27(y,func_27_,gfunc_27_,hess_27_,t,d)
x[0] = 1 / (96.05 * (y[1] + 1))
x[1] = x[0] / y[0]
print("最值点为：")
print(x, '\n')
x=np.array([-0.01,500])
y=np.array([0.,0.])
y[0]=x[0]/x[1]
y[1]=1/(96.05*x[0])-1
print("初始点为：")
print(x,'\n')
t=np.array([2000,5000,10000,20000,30000,50000])
d=np.array([0.9427,0.8616,0.7384,0.5362,0.3739,0.3096])
y=GN27(y,func_27_,gfunc_27_,hess_27_,t,d)
x[0] = 1 / (96.05 * (y[1] + 1))
x[1] = x[0] / y[0]
print("最值点为：")
print(x, '\n')
print("di的标准差为:")
print(np.std(d))