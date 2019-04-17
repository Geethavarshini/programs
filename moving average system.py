import numpy as np
import matplotlib.pyplot as plt
p=input("enter the order of the moving average system")
fs=3000
f1=100
f2=400
y=np.zeros(200)
t=np.linspace(0,400,200)
u=np.sin(2*np.pi*f1*t/fs)
#v=np.sin(2*np.pi*f2*t/fs)
v=np.random.rand(len(u))
x=u+v
sum=0
for i in range(0,200):
	for k in range(0,4):
		sum=sum+x[i-k]
		print (sum)
	y[i]=float((sum)/(5))
	sum=0
print (y)
plt.subplot(4,1,1)
plt.stem(t,u)
plt.subplot(4,1,2)
plt.plot(t,v)
plt.subplot(4,1,3)
plt.plot(t,x)
plt.subplot(4,1,4)
plt.plot(t,y)
plt.show()
