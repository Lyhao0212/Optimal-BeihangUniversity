import numpy as np
from steepest import steepest
from function import func_6_,gfunc_6_,hess_6_



print("-----5.6-----\n")
x1=np.array([0,0])
x2=np.array([-0.4,0])
x3=np.array([10,0])
x4=np.array([11,0])

steepest(x1,func_6_,gfunc_6_,hess_6_)
steepest(x2,func_6_,gfunc_6_,hess_6_)
steepest(x3,func_6_,gfunc_6_,hess_6_)
steepest(x4,func_6_,gfunc_6_,hess_6_)
