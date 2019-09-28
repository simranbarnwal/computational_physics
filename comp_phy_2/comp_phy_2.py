################################################################################################
'''Name: Simran Barnwal'''
'''Roll: 150121044'''
################################################################################################

import sys
import math
import copy



#################___Printer____######################
def prin(A,n):
	print "\n..................................."
	print "This is the output\n"
	for i in range(n):
		print A[i] 
	print "...................................\n"

#################___Pivoting____########################
def pivot(A,B,n):
	for i in range(n):
		temp=i
		if A[i][i]==0:
			for j in range(i+1,n):
				if A[j][i]!=0:
					A[i],A[j]=A[j],A[i]
					B[j],B[i]=B[i],B[j]
					break		
			
	return A,B	

#################___Partial_Pivoting____########################
def ppivot(A,B,n):
	for i in range(n):
		c=i
		for j in range(i+1,n):
			if ((abs(A[j][i])<abs(A[i][i]))&(A[j][i]!=0)):
				c=j

		if c!=i: 
			d=A[j][i]/A[i][i]
			for p in range(i,n):
				A[i][p]=A[i][p]*d
			B[i]=d*B[i]
	return A,B				

#################___GuassE___#########################
def guasse(U,n):
	L=[[0.0 for i in range(n)]for j in range(n)]
	for i in range(n):
		for j in range(i+1,n):
			if U[j][i]!=0:			
				c=U[j][i]/U[i][i]
				for p in range(i,n):
					U[j][p]=U[j][p]-U[i][p]*c
				L[j][i]=c
	for i in range(n): L[i][i]=1
	return L,U

#################___Forward_sub___######################
def fore(L,B,n):
	X=[0 for i in range(n)]
	X[0]=B[0]/L[0][0]
	for i in range(n):
		temp=B[i]
		for j in range(i):
			temp=temp-L[i][j]*X[j]
		X[i]=temp/L[i][i]
	return X

#################___Backward_sub___######################
def back(U,X,n):
    
	Sol=[0 for i in range(n)]
	if U[n-1][n-1]!=0:
	    Sol[n-1]=X[n-1]/U[n-1][n-1]	
	for i in range(n-2,-1,-1):	
		temp=X[i]	
		for j in range(i+1,n):
			temp=temp-U[i][j]*Sol[j]	
		if U[i][i]!=0:
		    Sol[i]=temp/U[i][i]	

	return Sol

#####################___Inverse___#############################
def inv(L,U,n):
	Inv=[]
	Inv=[[0 for i in range(n)]for j in range(n)]
	Invv=[]
	Invv=[[0 for i in range(n)]for j in range(n)]
	Invf=[]
	Invf=[[0 for i in range(n)]for j in range(n)]
	Sol=[]
	Sol=[[0 for i in range(n)]for j in range(n)]
	for i in range(n):
		Sol[i][i]=1
	for i in range(n):
		Invv[i]=fore(L,Sol[i],n)
		Inv[i]=back(U,Invv[i],n)

	for i in range(n):
		for j in range(n):
			Invf[i][j]=Inv[j][i]	
	return Invf	
######################__DO_little__#############################
def dolittle():
	
	filename = 'input.txt'
	input_filename=open(filename)
	with input_filename as f:
		inp = f.readlines()
	inp = [x.strip().split(" ") for x in inp]

	m=int(inp[0][0])
	
	A=[];C=[];
	A = [[0 for i in range(m)] for j in range(m)]
	B=[];L=[];U=[];X=[];Sol=[];Inv=[];
	print "\nPlease enter matrix"
	for i in range(m+1):
		if i!=m:		
			A[i]=map(float, inp[i+1])
		if i==m:
			B=map(float, inp[i+1])	

	C=copy.deepcopy(A)	

	A,B=pivot(A,B,m)
	#A,B=ppivot(A,B,m)
	
	L,U=guasse(A,m)
	X=fore(L,B,m)
	Sol=back(U,X,m)

	print "\nMatrix L:\n",('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in L]))
	print "\nMatrix U:\n",('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in U]))	

	print "\nThe loong wait has completed\n"
	q=-1
	for i in range(m):
		if U[i][i]==0:
			q=0
	if q==0:
		print "Sorry no solution\n"
	else:
		for i in range(m):
			print round(Sol[i], 6)    
	
	print "\nNow for the inverse matrix"	
	Inv=inv(L,U,m)
	
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Inv]))
	
	Final=[]
	Final=[[0.0 for i in range(m)]for j in range(m)]
	print "\nPrinting A*A(inv)"
	for i in range(m):
		for j in range(m):
			for k in range(m):
				Final[i][j]=Final[i][j]+C[i][k]*Inv[k][j]
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Final]))		
	
	print "\nPrinting LU\n"
	Final=[[0.0 for i in range(m)]for j in range(m)]
	for i in range(m):
		for j in range(m):
			for k in range(m):
				Final[i][j]=Final[i][j]+L[i][k]*U[k][j]
	
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Final]))		
	
	
				
####################___Cheloski___########################		
def chelk():

	filename = 'input1.txt'
	input_filename=open(filename)
	with input_filename as f:
		inp = f.readlines()
	inp = [x.strip().split(" ") for x in inp]

	m=int(inp[0][0])
	A=[]
	A = [[0 for i in range(m)] for j in range(m)]
	for i in range(m):
		A[i]=map(float, inp[i+1])
	
	B=[];L=[];X=[];Sol=[];LT=[];
	L=[]
	L=[[0 for i in range(m)]for j in range(m)]
	LT=[[0 for i in range(m)]for j in range(m)]
	L[0][0]=A[0][0]**(0.5)
	
	#Doing for off diagonal elements and diagonal sepertely using if else
	
	for i in range(1,m):
		for j in range(i+1):
			temp=A[i][j]
			if i==j:
				for k in range(i):
					temp=temp-(L[i][k]**(2.0))
				L[i][i]=(temp)**(0.5)	
			if i!=j:
				for k in range(j):
					temp=temp-L[i][k]*L[j][k]
				L[i][j]=temp/L[j][j]
	
	for i in range(m):
		for j in range(m):
			LT[i][j]=L[j][i]
			
	print "\n\nLong wait is over \n"
	print "The solution is: L="
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in L]))
	print "\nThe solution is: LT="
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in LT]))

	Final=[]
	Final=[[0.0 for i in range(m)]for j in range(m)]
	for i in range(m):
		for j in range(m):
			for k in range(m):
				Final[i][j]=Final[i][j]+L[i][k]*LT[k][j]
	
	
	print "\nMultiplying L and LT="
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Final]))		
	

	
				
#####################___Main__Prog__##########################

print "\nPlease choose method"
print "Enter 1 for dolittle and 2 for chowelski"
x=int(raw_input().strip())
if x==1:
	dolittle()
if x==2:
	chelk()
'''
3.0 -0.1 -0.2
0.1 7.0 -0.3
0.3 -0.2 10.0
7.85 -19.3 71.4	

4 3 2 1
3 3 2 1
2 2 2 1
1 1 1 1
'''
