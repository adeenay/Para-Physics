import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter

k=16
d=8

M=20+1
N=20+1

r_c = 0.5

X=np.zeros((N*d,M*k),dtype=float)
Y=np.zeros((N*d,M*k),dtype=float)
U=np.zeros((N*d,M*k),dtype=float)
V=np.zeros((N*d,M*k),dtype=float)
P=np.zeros((N*d,M*k),dtype=float)
T=np.zeros((N*d,M*k),dtype=float)
W=np.zeros((N*d,M*k),dtype=float)
R=np.zeros((N*d,M*k),dtype=float)

for i in range(0,k*d):
	
	if(i<=9):
		x=np.loadtxt('X000%d.dat' % i)
		y=np.loadtxt('Y000%d.dat' % i)
		u=np.loadtxt('U000%d.dat' % i)
		v=np.loadtxt('V000%d.dat' % i)
        	p=np.loadtxt('P000%d.dat' % i)
                t=np.loadtxt('T000%d.dat' % i)
		w=np.loadtxt('W000%d.dat' % i)
		r=np.loadtxt('R000%d.dat' % i)
	elif(i<=99):
		x=np.loadtxt('X00%d.dat' % i)
		y=np.loadtxt('Y00%d.dat' % i)
		u=np.loadtxt('U00%d.dat' % i)
		v=np.loadtxt('V00%d.dat' % i)
		p=np.loadtxt('P00%d.dat' % i)
                t=np.loadtxt('T00%d.dat' % i)
		w=np.loadtxt('W00%d.dat' % i)
		r=np.loadtxt('R00%d.dat' % i) 
	elif(i<=999):
		x=np.loadtxt('X0%d.dat' % i)
		y=np.loadtxt('Y0%d.dat' % i)
		u=np.loadtxt('U0%d.dat' % i)
		v=np.loadtxt('V0%d.dat' % i)
		p=np.loadtxt('P0%d.dat' % i)
                t=np.loadtxt('T0%d.dat' % i)
		w=np.loadtxt('W0%d.dat' % i)
		r=np.loadtxt('R0%d.dat' % i)
	else:
		x=np.loadtxt('X%d.dat' % i)
		y=np.loadtxt('Y%d.dat' % i)
		u=np.loadtxt('U%d.dat' % i)
		v=np.loadtxt('V%d.dat' % i)
		p=np.loadtxt('P%d.dat' % i)
                t=np.loadtxt('T%d.dat' % i)
		w=np.loadtxt('W%d.dat' % i)
		r=np.loadtxt('R%d.dat' % i)

	x=np.reshape(x,[N,M])
	y=np.reshape(y,[N,M])
	u=np.reshape(u,[N,M])
	v=np.reshape(v,[N,M])
        p=np.reshape(p,[N,M])
        t=np.reshape(t,[N,M])
	w=np.reshape(w,[N,M])
	r=np.reshape(r,[N,M])

	X[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=x
	Y[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=y
	U[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=u
	V[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=v
        P[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=p
	T[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=t
	W[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=w
	R[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=r


x_c = np.linspace(-r_c,r_c,200)
y_c = np.sqrt(r_c**2-x_c**2)

x_circle = np.concatenate([x_c,np.fliplr([x_c[:-1]])[0]]) + 3.0
y_circle = np.concatenate([y_c,-np.fliplr([y_c[:-1]])[0]])  

level_max =  5
level_min = -level_max

for i in range(0,N*d):
	for j in range(0,M*k):
		if(W[i][j] >= level_max):
			W[i][j] = level_max
		if(W[i][j] <= level_min):
			W[i][j] = level_min

plt.figure()
plt.title('Temperature')
plt.contourf(X,Y,T,100,density=5)
plt.plot(X[:,0],Y[:,0],'k')
plt.plot(X[:,-1],Y[:,-1],'k')
plt.plot(X[0,:],Y[0,:],'k')
plt.plot(X[-1,:],Y[-1,:],'k')
plt.xlabel('X')
plt.ylabel('Y')
plt.fill(x_circle,y_circle,'w')
plt.plot(x_circle,y_circle,'k')
plt.colorbar()
plt.axis('equal')

plt.figure()
plt.title('Vorticity')
plt.contourf(X,Y,W,100,density=5)
plt.plot(X[:,0],Y[:,0],'k')
plt.plot(X[:,-1],Y[:,-1],'k')
plt.plot(X[0,:],Y[0,:],'k')
plt.plot(X[-1,:],Y[-1,:],'k')
plt.xlabel('X')
plt.ylabel('Y')
plt.fill(x_circle,y_circle,'w')
plt.plot(x_circle,y_circle,'k')
plt.axis('equal')

plt.figure()
plt.title('Density')
plt.contourf(X,Y,R,100,density=5)
plt.plot(X[:,0],Y[:,0],'k')
plt.plot(X[:,-1],Y[:,-1],'k')
plt.plot(X[0,:],Y[0,:],'k')
plt.plot(X[-1,:],Y[-1,:],'k')
plt.xlabel('X')
plt.ylabel('Y')
plt.fill(x_circle,y_circle,'w')
plt.plot(x_circle,y_circle,'k')
plt.colorbar()
plt.axis('equal')

plt.show()
