from function import func_7_,gfunc_7_,hess_7_
from Newton import Newton7
import warnings
warnings.filterwarnings("ignore")



print("-----5.7-----\n")
x1=7.4
x2=7.2
x3=7.01
x4=7.8
x5=7.88
Newton7(x1,func_7_,gfunc_7_,hess_7_)
Newton7(x2,func_7_,gfunc_7_,hess_7_)
Newton7(x3,func_7_,gfunc_7_,hess_7_)
Newton7(x4,func_7_,gfunc_7_,hess_7_)
Newton7(x5,func_7_,gfunc_7_,hess_7_)