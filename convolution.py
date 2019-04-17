import numpy as np
import matplotlib.pyplot as plt
n=input('enter length of x')
k=input('enter length of h')
x=[]
h=[]
y=[]

for i in range(int(n)):
  m=input('enter elements')
  x.append(m)
for j in range(int(k)):
     p=input('enter elements')
     h.append(p)
print(x)
print(h)
z=int(n)+int(k)-1
while(int(n)<int(z)):
   x.append(0)
   n=int(n)+1
   d=len(x)
for i in range(int(z)):
  s=0
  for j in range(int(k)):
     a=int(x[i-j])*int(h[j])
     s=s+a
  y.append(s)
plt.stem(y)
print(y)
plt.show()
