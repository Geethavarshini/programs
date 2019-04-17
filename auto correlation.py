import numpy as np
import matplotlib.pyplot as plt
m=input("enter length of x:")
x=[]
x1=[]
y=[]
z=m
p=2*z-1
print p
n=np.arange(0,p , 1)
for i in range(m):
	c=input("enter an element:")
	x.append(c)
for i in range(m):
	k=x[m-1-i]
	x1.append(k)
while(m<p):
	x.append(0)
	m=m+1
for i in range(p):
	s=0
	for j in range(z):
		q=x1[j]*x[i-j]
		s=s+q
	y.append(s)
plt.stem(n,y)
plt.show()
	
