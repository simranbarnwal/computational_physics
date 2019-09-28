################################################################################################
'''Name: Simran Barnwal'''
'''Roll: 150121044'''
################################################################################################

import math

###############################################################################################################

def func(x,a,b):
	f_x=0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
	return f_x

###############################################################################################################

def trap(a,b):
	I=(b-a)*(func(a,a,b)+func(b,a,b))*0.5
	return I

###############################################################################################################

def trap_m(X,n,a,b):
	summ=0
	for i in range(n-1):
		summ+=func(X[i+1],a,b)
	I=(b-a)*(func(a,a,b)+func(b,a,b)+2*summ)/2/n
	return I

###############################################################################################################

def randm(x):
	x=x*100
	c=69
	d=15
	m=80
	xx=(c*x+d)%m
	return xx/100

###############################################################################################################

def smean(n,a,b):
	XX=[0.0 for i in range(n+1)]
	XX[0]=0.4			#	Guess value	
	for i in range(n):
		XX[i+1]=randm(XX[i])
#	print "\nPrinting XX", XX	
	temp=0
	for i in range(n+1):
		temp+=func(XX[i],a,b)	
	temp=temp/n
	I=(b-a)*temp
	return I	

###############################################################################################################

a=0
b=0.8
print "\nPlease enter number of points to be plotted"
n=int(raw_input().strip())
X=[0.0 for i in range(n+1)]
h=(b-a)/n
print "\n Printing n", n

for i in range(n+1):
	X[i]=a+i*h

#print "\nPrinting x values", X

print "\n\nIntegral from trapezoid : ", trap(a,b)
print "\n\nIntegral from trapezoid multiple : ", trap_m(X,n,a,b)
print "\n\nIntegral from sample mean : ", smean(n,a,b), "\n"












