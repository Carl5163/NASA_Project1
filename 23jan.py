import matplotlib.pyplot as plt
import numpy as np
# Solve the DE y''(t)+y(t)=0, y(0)=0, y'(0)=1
#
# Y_1 = y
# Y_2 = y'
#
# Y_1' = y' = Y_2; Y_1(0)=0
# Y_2' = y'' = -Y_1; Y_2(0)=1 (from the DE)
#

#Stepsize
h=0.01

#x-value array
xvals=np.arange(0,10,h)

#Solution arrays
Y1=[0]
Y2=[1]

#RHS of the 1st order eqts
def f(x,y1,y2):
	return y2
def g(x,y1,y2):
	return -y1

# k functions
def k1(xn,y1n,y2n):
	return h*f(xn,y1n,y2n)
def k2(xn,y1n,y2n):
	return h*f(xn+h/2,y1n+k1(xn,y1n,y2n)/2, y2n+l1(xn,y1n,y2n)/2)
def k3(xn,y1n,y2n):
        return h*f(xn+h/2,y1n+k2(xn,y1n,y2n)/2, y2n+l2(xn,y1n,y2n)/2)
def k4(xn,y1n,y2n):
	return h*f(xn+h,y1n+k3(xn,y1n,y2n), y2n+l3(xn,y1n,y2n))
def k(xn,y1n,y2n):
	return (1.0/6.0)*(k1(xn,y1n,y2n)+2*k2(xn,y1n,y2n)+2*k3(xn,y1n,y2n)+k4(xn,y1n,y2n))

# l functions
def l1(xn,y1n,y2n):
        return h*g(xn,y1n,y2n)
def l2(xn,y1n,y2n):
        return h*g(xn+h/2,y1n+k1(xn,y1n,y2n)/2, y2n+l1(xn,y1n,y2n)/2)
def l3(xn,y1n,y2n):
        return h*g(xn+h/2,y1n+k2(xn,y1n,y2n)/2, y2n+l2(xn,y1n,y2n)/2)
def l4(xn,y1n,y2n):
        return h*g(xn+h,y1n+k3(xn,y1n,y2n), y2n+l3(xn,y1n,y2n))
def l(xn,y1n,y2n):
        return (1.0/6.0)*(l1(xn,y1n,y2n)+2*l2(xn,y1n,y2n)+2*l3(xn,y1n,y2n)+l4(xn,y1n,y2n))

n=0
while(n<len(xvals)-1):
	Y1.append(Y1[n]+k(xvals[n],Y1[n],Y2[n]))
	Y2.append(Y2[n]+l(xvals[n],Y1[n],Y2[n]))
	n+=1

print k1(0,0,1)
print k2(0,0,1)
print k3(0,0,1)
print k4(0,0,1)
print k(0,0,1)

plt.plot(xvals,Y1)
plt.show()
	

