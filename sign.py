import numpy as np
x=np.arange(21)
print("before changing the sign",x)
x[(x>=9)&(x<18)] *=-1
print("after changing the sign",x)