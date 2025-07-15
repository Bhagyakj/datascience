import numpy as np
x=np.array([[1,2,3],[4,5,6]])
print(x)
print("sum of all elements")
print(np.sum(x))
print("sum of elements of column")
print(np.sum(x,axis=0))
print("sum of elements of row")
print(np.sum(x,axis=1))