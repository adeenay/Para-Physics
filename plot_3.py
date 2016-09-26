import matplotlib.pyplot as plt
import numpy as np

k=2
d=1

M=20+1
N=20+1

X=np.zeros((N*d,M*k),dtype=float)
Y=np.zeros((N*d,M*k),dtype=float)
U=np.zeros((N*d,M*k),dtype=float)
V=np.zeros((N*d,M*k),dtype=float)
P=np.zeros((N*d,M*k),dtype=float)
T=np.zeros((N*d,M*k),dtype=float)

for i in range(0,k*d):
	
	if(i<=9):
		x=np.loadtxt('X0%d.dat' % i)
		y=np.loadtxt('Y0%d.dat' % i)
		u=np.loadtxt('U0%d.dat' % i)
		v=np.loadtxt('V0%d.dat' % i)
        	p=np.loadtxt('P0%d.dat' % i)
                t=np.loadtxt('T0%d.dat' % i)
	else:
		x=np.loadtxt('X%d.dat' % i)
		y=np.loadtxt('Y%d.dat' % i)
		u=np.loadtxt('U%d.dat' % i)
		v=np.loadtxt('V%d.dat' % i)
		p=np.loadtxt('P%d.dat' % i)
                t=np.loadtxt('T%d.dat' % i)
        
	x=np.reshape(x,[N,M])
	y=np.reshape(y,[N,M])
	u=np.reshape(u,[N,M])
	v=np.reshape(v,[N,M])
        p=np.reshape(p,[N,M])
        t=np.reshape(t,[N,M])
		
	X[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=x
	Y[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=y
	U[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=u
	V[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=v
        P[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=p
	T[(i/k)*N:(i/k)*N+N,(i%k)*M:(i%k)*M+M]=t

"""
plt.figure()
plt.title('V Velocity')
#plt.title('Re = 1000, Grid = 128 x 128, Solver = FORTRAN')
#plt.contourf(X,Y,V,density=5)
plt.streamplot(X,Y,U,V,density=5)
plt.plot(X[:,0],Y[:,0],'k')
plt.plot(X[:,-1],Y[:,-1],'k')
plt.plot(X[0,:],Y[0,:],'k')
plt.plot(X[-1,:],Y[-1,:],'k')
#plt.plot(X,Y,'g')
#plt.plot(X.T,Y.T,'g')
#plt.ylim(-0.2,1.2)
#plt.xlim(-0.2,2.2)
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')

plt.figure()
plt.title('U Velocity')
plt.contourf(X,Y,U,density=5)
plt.plot(X[:,0],Y[:,0],'k')
plt.plot(X[:,-1],Y[:,-1],'k')
plt.plot(X[0,:],Y[0,:],'k')
plt.plot(X[-1,:],Y[-1,:],'k')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')

"""
Dataout = np.row_stack((T[:,3]))
np.savetxt('Parasolve.dat',Dataout)

#Dataout = np.row_stack((Y[:,3]))
#np.savetxt('Parasolve_Y.dat',Dataout)

plt.figure()
plt.title('Distance Function')
plt.contourf(X,Y,U,density=20)
plt.plot(X[:,0],Y[:,0],'k')
plt.plot(X[:,-1],Y[:,-1],'k')
plt.plot(X[0,:],Y[0,:],'k')
plt.plot(X[-1,:],Y[-1,:],'k')
plt.plot(X,Y,'g')
plt.plot(X.T,Y.T,'g')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal') 

plt.figure()
plt.title('Thermal Conductivity')
plt.contourf(X,Y,P,density=5)
plt.plot(X[:,0],Y[:,0],'k')
plt.plot(X[:,-1],Y[:,-1],'k')
plt.plot(X[0,:],Y[0,:],'k')
plt.plot(X[-1,:],Y[-1,:],'k')
plt.plot(X,Y,'g')
plt.plot(X.T,Y.T,'g')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal') 

plt.figure()
plt.title('Temperature')
plt.contourf(X,Y,T,density=5)
#plt.streamplot(X,Y,U,V,density=4,color='k')
plt.plot(X[:,0],Y[:,0],'k')
plt.plot(X[:,-1],Y[:,-1],'k')
plt.plot(X[0,:],Y[0,:],'k')
plt.plot(X[-1,:],Y[-1,:],'k')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.show()
