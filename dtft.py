import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
#x=[2,14,21,6,12,5,4,0,10,3]
x=[1,1,1,1,1,]
j=cm.sqrt(-1)
l=len(x)
y=[]
w=np.linspace(-np.pi,np.pi,1000)
for i in range(0,1000):
  w1=w[i]
  s=0
  for k in range(0,l):
    s+=(x[k]*np.exp(-j*w1*k))
  y.append(s)
y1=np.abs(y)
y2=np.angle(y)
plt.subplot(3,1,1)
plt.plot(w,y)
plt.subplot(3,1,2)
plt.plot(w,y1)
plt.subplot(3,1,3)
plt.plot(w,y2)
plt.show()
