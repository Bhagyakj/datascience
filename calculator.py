import numpy as np
from fontTools.cffLib.transforms import remove_unused_subroutines

print("Numpy Calculator")
print("select operation : ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("enter choice (1/2/3/4):")
num1=np.float64(input("Enter first number:"))
num2=np.float64(input("Enter second number:"))
if choice=='1':
    result=np.add(num1,num2)
    print("result :",result)
elif choice=='2':
    result=np.subtract(num1,num2)
    print("result :",result)
elif choice == '3':
    result = np.multiply(num1, num2)
    print("result :", result)
elif choice == '4':
    if num2 == 0:
        print("cannot divide by Zero !")
    else:
        result = np.divide(num1,num2)
        print("Result : ",result)
else:
    print("invalid input")
