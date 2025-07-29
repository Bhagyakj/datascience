import matplotlib.pyplot as plt
x1=[1,2,3,4]
y1=[10,20,25,30]

x2=[1,2,3,4]
y2=[30,23,15,10]
plt.plot(x1,y1,label='Line 1',color='blue',marker='o')
plt.plot(x2,y2,label='Line 2',color='green',marker='s')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines on Same Plot')
plt.legend()
plt.grid(True)
plt.savefig("p14.png")