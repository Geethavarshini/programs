import numpy as np
import matplotlib.pyplot as plt
sample=input("enter no. of samples")
x=np.arange(sample)
#y1=x*x
plt.plot(x,y1)
plt.xlabel('sample(n)')
plt.ylabel('sample(v)')
s=[]
for i in range(0,sample):
	y1=s[i]+i
	s.append(y1)
print(s)
len=len(s)
sum=[]
s2=0
for i in range (0,len):
	s2+=s[i]
	sum.append(s2)
plt.stem(i,sum)
plt.show()
