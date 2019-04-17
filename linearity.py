import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
j=cm.sqrt(-1)
def dft(x):
	u=len(x)
	X=[]
	for i in range(0,u):
	       s=0
	       for k in range(0,u):
		    s+=(x[k]*np.exp(-k*2*np.pi*i/u*j))
	       X.append(s)
	return X
a=[]
b=[]
x=[]
y1=[]
y2=[]
x1=[3,6,10,44,59,30,54,67,5,2,1]
x2=[1,2,3,4,5,6,7,8,9,10,33]
for i in range(11):
	s=x1[i]+x2[i]
	x.append(s)
	s=0
print x
a=dft(x1)
b=dft(x2)
y1=a+b
y2=dft(x)
m1=np.abs(y1)
m2=np.abs(y2)
plot.subplot(211)
plot.plot(m1,'g')
plot.subplot(212)
plot.plot(m2,'b')
plot.show()	
