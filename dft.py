import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
j=cm.sqrt(-1)
x=[4,5,8,1,3,9,10,25,33,20,3]
u=input("enter the N to find N pt DFT:")
N=len(x)
w=np.arange(0,u)
X=[]
Y=[]
while (N<u):
	x.append(0)
	N+=1
for i in range(0,u):
       s=0
       for k in range(0,N):
            s+=(x[k]*np.exp(-k*2*np.pi*i/N*j))
       X.append(s)
for i in range(0,N):
       s=0
       for k in range(0,N):
            s+=(x[k]*np.exp(-k*2*np.pi*i/N*j))
       Y.append(s)
print x
m=np.abs(X)
p=np.angle(X)
m1=np.abs(Y)
p1=np.angle(Y)
plot.subplot(231)
plot.stem(w,Y,'r')
plot.subplot(232)
plot.stem(w,m1,'b')
plot.subplot(233)
plot.stem(w,p1,'g')
plot.subplot(234)
plot.stem(w,X,'r')
plot.subplot(235)
plot.stem(w,m,'b')
plot.subplot(236)
plot.stem(w,p,'g')
plot.show()
