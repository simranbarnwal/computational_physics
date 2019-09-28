import sys
import math
import copy

#######################__Jacobi____###########################

def Jacobi(A,tol,n):
	t=0.0
	c=0.0
	s=0.0
	D=[[0.0 for i in range(n)]for j in range(n)]
	w=1
	print "\nPrinting index",n
	count=0
	while w==1:
		D=copy.deepcopy(A)
		count=count+1
		p=0;q=0;

		temp=0.0
		for i in range(n):
			for j in range(n):
				if i!=j:
					if abs(A[i][j])>abs(temp):
						temp=copy.deepcopy(A[i][j])
						p=i
						q=j
		if (p==0)and(q==0):
			break
		theta=(A[q][q]-A[p][p])/(2*A[p][q]) 
		if theta!=0:
			t=(theta/abs(theta))/((abs(theta)+((theta**2)+1)**0.5))
		else:
			t=1
		c=1/((1+t**2)**0.5)
		s=c*t		
		for i in range(n):
			if (i!=p)and(i!=q):
				D[i][p]=c*A[i][p]-s*A[i][q]
				D[i][q]=s*A[i][p]+c*A[i][q]
				D[p][i]=D[i][p]				
				D[q][i]=D[i][q]

		D[p][p]=c*c*A[p][p]+s*s*A[q][q]-2*c*s*A[p][q]
		D[q][q]=c*c*A[q][q]+s*s*A[p][p]+2*c*s*A[p][q]
		D[p][q]=0.0
		D[q][p]=0.0
		
		A=copy.deepcopy(D)		

		if abs(temp)<tol:		
			w=0
	return D	

#################___Base_Hamiltonian__######################

def Ho(n):
	a=0.5
	A=[[0.0 for i in range(n)]for j in range(n)]
	for i in range(n):
		A[i][i]=a
		a=a+1

	return A
		
################___creati0n____########################

def cre(n):
	ad=[[0.0 for i in range(n)]for j in range(n)]
	for i in range(n-1):
		ad[i+1][i]=(i+1)**(0.5)

	return ad

################___distructi0n____########################

def des(n):
	a=[[0.0 for i in range(n)]for j in range(n)]
	for i in range(n-1):
		a[i][i+1]=(i+1)**(0.5)

	return a

################___perturbed_hamiltonian__###############

def pert(lamda,ho,T,n):
	order=4
	H=[];
	H=copy.deepcopy(ho)
	X=[[0.0 for i in range(n)]for j in range(n)]
	Y=copy.deepcopy(T)
	for i in range(order-1):
		X=[[0.0 for i in range(n)]for j in range(n)]
		for j in range(n):
			for k in range(n):
				for l in range(n):
					X[j][k]=X[j][k]+Y[j][l]*T[l][k]
		Y=copy.deepcopy(X)
	for i in range(n):
		for j in range(n):
			H[i][j]=H[i][j]+lamda*Y[i][j]

	return H	
		
	
#################__Main__#############################

print "\nPLease enter tolerance"
x=int(raw_input().strip())
z=1.0
for i in range(x):
	z=z/10
print "\nPlease enter dimension"
n=int(raw_input().strip())
A=[];T=[];H=[];
T=[[0.0 for i in range(n)]for j in range(n)]

A=Ho(n)
print "\nBare matrix"
for i in range(n):
	print A[i]
a=des(n)
ad=cre(n)
for i in range(n):
	for j in range(n):
		T[i][j]=(a[i][j]+ad[i][j])/(2**0.5)
print "\nX matrix"
for i in range(n):
	print T[i]
E=[0.0 for j in range(n)]
lamda=0.0
f=open('output.txt','w')
g=open('output1.txt','w')
for i in range(11):
	H=pert(lamda,A,T,n)
	print "\n",lamda,"\n"
	print('\n'.join([''.join(['{:12}'.format(round(item, 6)) for item in row])for row in H]))		
	
	D=Jacobi(H,z,n)
	for j in range(n):
		E[j]=D[j][j]
	E.sort()	
	print "\n\n\nFinal Jacobi matrix"
	print('\n'.join([''.join(['{:25}'.format(round(item, 15)) for item in row])for row in D]))		
	f.write(str(lamda))
	for j in range(n):
		f.write(" ")
		f.write(str(E[j]))
	f.write("\n")
	
	lamda=lamda+0.1	

#p "output.txt"u 1:2 w lp,"output.txt"u 1:3 w lp,"output.txt"u 1:4 w lp,"output.txt"u 1:5 w lp,"output.txt"u 1:2 w lp, "output.txt"u 1:6 w lp


