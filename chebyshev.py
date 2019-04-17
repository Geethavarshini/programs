import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
dp=float(input("enter pb gain:"))
ds=float(input("enter sb gain:"))
wp=float(input("enter pb frq:"))
ws=float(input("enter sb freq:"))

e=((1/dp**2)-1)**0.5
print(e)

x=((1/ds**2)-1)**0.5
g=np.arccosh(x/e)
m=np.arccosh(ws/wp)
c=(g/m)
N=np.ceil(c)
print(N)

k=cm.sqrt(1+e**2)+(1/e)
YN=0.5*(k**(1/N)-k**(-1/N))
print(YN)

w=np.arange(0,10000)
mag=[]
for i in range(0,10000):
	b=(e**2)*(np.cosh(N*np.arccosh(i/wp)))**2
	Hs=1/(cm.sqrt(1+b))
	mag.append(np.abs(Hs))
print (mag)
mag1=[]
for i in range(0,10000):
	b=(e**2)*(np.cos(N*np.arccos(i/wp)))**2
	Hs=1/(cm.sqrt(1+b))
	mag1.append(np.abs(Hs))
plt.plot(w,mag)
plt.plot(w,mag1)
plt.show()
	














