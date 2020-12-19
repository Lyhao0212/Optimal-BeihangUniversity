import numpy as np
from function import func_4_,gfunc_4_,hess_4_
from TrustRegion import TR
import warnings
warnings.filterwarnings("ignore")

print("-----6.4-----")

n=10
print("----------n=",n,"时----------")
x=np.zeros(2*n).reshape(2*n,1)
TR(x,n,func_4_,gfunc_4_,hess_4_)

n=50
print("----------n=",n,"时----------")
x=np.zeros(2*n).reshape(2*n,1)
TR(x,n,func_4_,gfunc_4_,hess_4_)