import numpy as np
from conjugate_gradien import ConhugateGradient,\
                              Creatb,\
                              CreatHilbert

print("-----5.19-----\n")

print("----------n=5----------")
N1=5
G1=CreatHilbert(N1)
b1=Creatb(N1)
x1= np.zeros(N1).reshape(N1,1)
ConhugateGradient(x1,G1,b1)

print("----------n=8----------")
N2=8
G2=CreatHilbert(N2)
b2=Creatb(N2)
x2= np.zeros(N2).reshape(N2,1)
ConhugateGradient(x2,G2,b2)

print("----------n=12----------")
N3=12
G3=CreatHilbert(N3)
b3=Creatb(N3)
x3= np.zeros(N3).reshape(N3,1)
ConhugateGradient(x3,G3,b3)

print("----------n=20----------")
N4=20
G4=CreatHilbert(N4)
b4=Creatb(N4)
x4= np.zeros(N4).reshape(N4,1)
ConhugateGradient(x4,G4,b4)
