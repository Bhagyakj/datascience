import numpy as np
arr=np.arange(1,17,dtype='int').reshape(-1,4)
print("original array")
print(arr)
arr=arr[[-1,1,2,0]]
print("after swapping the array\n",arr)