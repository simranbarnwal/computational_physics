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
def pivot(A,n):
	for i in range(n):
		temp=i
		if A[i][i]==0:
			for j in range(i+1,n):
				if A[j][i]!=0:
					A[i],A[j]=A[j],A[i]
					break		
			
	return A	

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
	Invf=[]
	Invf=[[0 for i in range(n)]for j in range(n)]
	Sol=[]
	Sol=[[0 for i in range(n)]for j in range(n)]
	for i in range(n):
		Sol[i][i]=1
	for i in range(n):
		Inv[i]=fore(L,Sol[i],n)
		Inv[i]=back(U,Inv[i],n)

	for i in range(n):
		for j in range(n):
			Invf[i][j]=Inv[j][i]	
	return Invf	
######################__Small input__#############################
def power(itt):
	
	filename = 'input.txt'
	input_filename=open(filename)
	with input_filename as f:
		inp = f.readlines()
	inp = [x.strip().split(" ") for x in inp]

	n=int(inp[0][0])
	m=n
	A=[];C=[];
	A = [[0 for i in range(n)] for j in range(n)]
	L=[];U=[];X=[];Sol=[];Inv=[];
	for i in range(n+1):
		if i!=n:		
			A[i]=map(float, inp[i+1])
		
# Finished taking input

	C=copy.deepcopy(A)	

	A=pivot(A,n)	
	L,U=guasse(A,n)

# Finished LU decomp for inversion
	
	print "\nMatrix L:\n",('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in L]))
	print "\nMatrix U:\n",('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in U]))	

	Inv=inv(L,U,n)
	D=copy.deepcopy(Inv)	

# Inverse ready
	
	print "\nMatrix Inverse:\n",('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Inv]))
	
# Checking if inverse is proper

	Final=[]
	Final=[[0.0 for i in range(m)]for j in range(m)]
	print "\nPrinting A*A(inv)"
	for i in range(m):
		for j in range(m):
			for k in range(m):
				Final[i][j]=Final[i][j]+C[i][k]*Inv[k][j]
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Final]))		
	
	print "\nPrinting LU\n"
	Final=[[0.0 for i in range(n)]for j in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				Final[i][j]=Final[i][j]+L[i][k]*U[k][j]
	
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Final]))		
	
        print "\nPrinting the maximum eigen value"
        x=[]
	x=[2.0 for i in range(n)]
        y=[]
	y=[0.0 for i in range(n)]

	for i in range(itt):
		y=[0.0 for p in range(n)]
        	for j in range(n):
        		for k in range(n):
                	        y[j]=y[j]+C[j][k]*x[k]
              	x=y
		
                temp=x[0]
                for j in range(n):
                	if abs(temp)<abs(x[j]):
                	        temp=x[j]
				
                for k in range(n):
                	x[k]=x[k]/temp
		print "\n",x	
        print "\nNow finding the eigen value  "
	y=[0.0 for i in range(n)]

        for i in range(n):
         	for j in range(n):
         	       y[i]=y[i]+C[i][j]*x[j]
        lamda=y[0]/x[0] #check if zeroth entry is non zero
                
        x=[2.0 for i in range(n)]
	y=[0.0 for i in range(n)]
	
	for i in range(itt):
		y=[0.0 for p in range(n)]        
		for j in range(n):
                	for k in range(n):
                        	y[j]=y[j]+D[j][k]*x[k]
        	x=y
                temp=x[0]
        	for j in range(n):
        		if abs(temp)<abs(x[j]):
        		        temp=x[j]
       		for k in range(n):
        		x[k]=x[k]/temp
		
        print "\nNow finding the eigen value  "
	y=[0.0 for i in range(n)]	
        	        
	for i in range(n):
		for j in range(n):
        	        y[i]=y[i]+D[i][j]*x[j]
        lamdaa=y[0]/x[0] #check if zeroth entry is non zero
        lamdaa=1/lamdaa
        print "\nThe values you have been calculated"
        print "Max:  ",lamda
        print "Min:  ",lamdaa       
######################__Big input__#############################
def powerr(itt):
	
	filename = 'input1.txt'
	input_filename=open(filename)
	with input_filename as f:
		inp = f.readlines()
	inp = [x.strip().split(" ") for x in inp]

	n=int(inp[0][0])
	m=n
	A=[];C=[];
	A = [[0 for i in range(n)] for j in range(n)]
	L=[];U=[];X=[];Sol=[];Inv=[];
	for i in range(n+1):
		if i!=n:		
			A[i]=map(float, inp[i+1])
		
# Finished taking input

	C=copy.deepcopy(A)	

	A=pivot(A,n)	
	L,U=guasse(A,n)

# Finished LU decomp for inversion
	
	print "\nMatrix L:\n",('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in L]))
	print "\nMatrix U:\n",('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in U]))	

	Inv=inv(L,U,n)
	D=copy.deepcopy(Inv)	

# Inverse ready
	
	print "\nMatrix Inverse:\n",('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Inv]))
	
# Checking if inverse is proper

	Final=[]
	Final=[[0.0 for i in range(m)]for j in range(m)]
	print "\nPrinting A*A(inv)"
	for i in range(m):
		for j in range(m):
			for k in range(m):
				Final[i][j]=Final[i][j]+C[i][k]*Inv[k][j]
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Final]))		
	
	print "\nPrinting LU\n"
	Final=[[0.0 for i in range(n)]for j in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				Final[i][j]=Final[i][j]+L[i][k]*U[k][j]
	
	print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in Final]))		
	
        print "\nPrinting the maximum eigen value"
        x=[]
	x=[2.0 for i in range(n)]
        y=[]
	y=[0.0 for i in range(n)]

	for i in range(itt):
		y=[0.0 for p in range(n)]
        	for j in range(n):
        		for k in range(n):
                	        y[j]=y[j]+C[j][k]*x[k]
              	x=y
		
                temp=x[0]
                for j in range(n):
                	if abs(temp)<abs(x[j]):
                	        temp=x[j]
				
                for k in range(n):
                	x[k]=x[k]/temp
		print "\n",x	
        print "\nNow finding the eigen value  "
	y=[0.0 for i in range(n)]

        for i in range(n):
         	for j in range(n):
         	       y[i]=y[i]+C[i][j]*x[j]
        lamda=y[0]/x[0] #check if zeroth entry is non zero
                
        x=[2.0 for i in range(n)]
	y=[0.0 for i in range(n)]
	
	for i in range(itt):
		y=[0.0 for p in range(n)]        
		for j in range(n):
                	for k in range(n):
                        	y[j]=y[j]+D[j][k]*x[k]
        	x=y
                temp=x[0]
        	for j in range(n):
        		if abs(temp)<abs(x[j]):
        		        temp=x[j]
       		for k in range(n):
        		x[k]=x[k]/temp
		
        print "\nNow finding the eigen value  "
	y=[0.0 for i in range(n)]	
        	        
	for i in range(n):
		for j in range(n):
        	        y[i]=y[i]+D[i][j]*x[j]
        lamdaa=y[0]/x[0] #check if zeroth entry is non zero
        lamdaa=1/lamdaa
        print "\nThe values you have been calculated"
        print "Max:  ",lamda
        print "Min:  ",lamdaa       
#####################___Main__Prog__##########################

print "\nPlease choose problem number"
print "Enter 1 for small and 2 for big"
x=int(raw_input().strip())
print "\nNumber of iterations required"
itt=int(raw_input().strip())
if x==1:
	power(itt)
if x==2:
	powerr(itt)

