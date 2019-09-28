################################################################################################
'''Name: Simran Barnwal'''
'''Roll: 150121044'''
################################################################################################

import math

#######################___Heun____####################
def heun(n,h):
	Y=[0.0 for i in range(n+1)]
	Y[0]=1.0
	for i in range(n):
		Y[i+1]=Y[i]+h/2*(slope(i*h)+slope((i+1)*h))
	return Y

#######################___Exact____####################
def exact(n,h):
	Y=[0.0 for i in range(n+1)]
	for i in range(n):
		Y[i]=-0.5*(i*h)**4+4*(i*h)**3-10*(i*h)**2+8.5*(i*h)+1
	return Y

######################____Euler___####################
def euler(n,h):
	Y=[0.0 for i in range(n+1)]
	Y[0]=1.0
	for i in range(n):
		Y[i+1]=Y[i]+h*slope(i*h)
#		print "\n",Y[i+1]," ",slope(i*h)
	return Y 

#####################____Function_____################
def slope(x):
	m=-2*x**3+12*x**2-20*x+8.5
	return m

#####################____Main_____####################

#print "\nPlease enter number of points for plotting:   "
#n=int(raw_input().strip())
#print "\n\nPlease enter step size:   "
#h=int(raw_input().strip())
h=0.5
n=9
Y1=heun(n,h)
Y2=euler(n,h)
Y3=exact(n,h)
f=open('output.txt','w')
for i in range(n):
	f.write(str(i*h))
	f.write(" ")
	f.write(str(Y3[i]))
	f.write(" ")
	f.write(str(Y1[i]))
	f.write(" ")	
	f.write(str(math.fabs(Y1[i]-Y3[i])*100/Y3[i]))
	f.write(" ")	
	f.write(str(Y2[i]))
	f.write(" ")	
	f.write(str(math.fabs(Y2[i]-Y3[i])*100/Y3[i]))
	f.write("\n")

# p "output.txt" u 1:2 w lp, "output.txt"u 1:3 w lp, "output.txt"u 1:4 w lp, "output.txt" u 1:5 w lp, "output.txt" u 1:6 w lp


