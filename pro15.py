import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[25,16,9,4,1]
y3=[2,3,5,7,11]
plt.figure(figsize=(8,8))
plt.subplot(3,1,1)
plt.plot(x,y1,'r-o')
plt.title('Square Numbers')
plt.ylabel('y1')
plt.subplot(3,1,2)
plt.plot(x,y2,'g--s')
plt.title('Reverse Square Numbers')
plt.ylabel('y2')
plt.subplot(3,1,3)
plt.plot(x,y3,'b-^')
plt.title('Prime Numbers')
plt.xlabel('x')
plt.ylabel('y3')
plt.tight_layout()
plt.savefig("pro15.png")
