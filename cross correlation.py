import numpy as np
import matplotlib.pyplot as plt
m=input("enter length of x:")
g=input("enter length of h:")
x=[]
x1=[]
h=[]
y=[]
z=m
p=z+g-1
n=np.arange(0,p , 1)
for i in range(z):
	d=input("enter an element:")
	h.append(d)
for i in range(m):
	c=input("enter an element:")
	x.append(c)
for i in range(m):
	k=x[m-1-i]
	x1.append(k)
while(g<p):
	h.append(0)
	g=g+1
for i in range(p):
	s=0
	for j in range(z):
		q=x1[j]*h[i-j]
		s=s+q
	y.append(s)
plt.stem(n,y)
plt.show()
	
