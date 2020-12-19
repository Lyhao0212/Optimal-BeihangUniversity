

import numpy as np
from steepest import steepest
from function import func_9_,gfunc_9_,hess_9_
from Newton import Newton


print("-----5.9-----\n")
x1 = np.array([1.2,1.2])
x2 = np.array([-1.2,1])
steepest(x1,func_9_,gfunc_9_)
#Newton(x1,func_9_,gfunc_9_,hess_9_)
steepest(x2,func_9_,gfunc_9_)
#Newton(x2,func_9_,gfunc_9_,hess_9_)

