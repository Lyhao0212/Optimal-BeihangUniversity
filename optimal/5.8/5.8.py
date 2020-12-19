import numpy as np
from function import func_8_,gfunc_8_,hess_8_
from Newton import NewtonLS,NewtonNoLS
import warnings
warnings.filterwarnings("ignore")

print("-----5.8-----\n")
x1=np.array([8,9])
x2=np.array([1,40])
x3=np.array([15,68.69])
x4=np.array([10,20])
u1=1
u2=0.1

'''
print("u=1,无线搜索")
NewtonNoLS(x1,func_8_,gfunc_8_,hess_8_,u1)
NewtonNoLS(x2,func_8_,gfunc_8_,hess_8_,u1)
NewtonNoLS(x3,func_8_,gfunc_8_,hess_8_,u1)
NewtonNoLS(x4,func_8_,gfunc_8_,hess_8_,u1)

print("u=0.1,无线搜索")
NewtonNoLS(x1,func_8_,gfunc_8_,hess_8_,u2)
NewtonNoLS(x2,func_8_,gfunc_8_,hess_8_,u2)
NewtonNoLS(x3,func_8_,gfunc_8_,hess_8_,u2)
NewtonNoLS(x4,func_8_,gfunc_8_,hess_8_,u2)
'''

print("u=1,有线搜索")
NewtonLS(x1,func_8_,gfunc_8_,hess_8_,u1)
NewtonLS(x2,func_8_,gfunc_8_,hess_8_,u1)
NewtonLS(x3,func_8_,gfunc_8_,hess_8_,u1)
NewtonLS(x4,func_8_,gfunc_8_,hess_8_,u1)


print("u=0.1,有线搜索")
NewtonLS(x1,func_8_,gfunc_8_,hess_8_,u2)
NewtonLS(x2,func_8_,gfunc_8_,hess_8_,u2)
NewtonLS(x3,func_8_,gfunc_8_,hess_8_,u2)
NewtonLS(x4,func_8_,gfunc_8_,hess_8_,u2)
