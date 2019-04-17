import numpy as np
import matplotlib.pyplot as plot
def but(Sp,Ss,Wp,Ws):
	H=[]
	M=[]
	e=((1/(Sp)**2)-1)**0.5
	x=0.5*np.log(((1/(Sp)**2)-1)/((1/(Ss)**2)-1))/np.log(Wp/Ws)
	y=(np.arccosh((1/e)*np.sqrt((1/(Sp)**2)-1)))/(np.arccosh(Ws/Wp))
	n=np.ceil(y)
	N=np.ceil(x)
	Wc=Wp/(((1/(Sp)**2)-1))**(1/2*N)
	w=3000
	print N,n
	for i in range(w):
		a=float(1/np.sqrt((1+(2*np.pi*i/Wc)**(2*N))))
		H.append(a)
	return H
	
Sp=0.8
Ss=0.2
Wp=4000*np.pi
Ws=5000*np.pi
H=[]
H=but(Sp,Ss,Wp,Ws)
plot.plot(H)
plot.show()

