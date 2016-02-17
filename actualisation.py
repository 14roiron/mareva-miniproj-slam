import numpy as np 
import matplotlib.pyplot as pyplot


vec = []
xbruit = [];
v=1;
w=0.1;

def init(x0,y0,teta0):
	x.append(x0);
	y.append(y0);
	teta.append(teta0);

def actualisation(v,w):
	global vec;
	vec.append([vec[0][-1]+v*np.cos(teta[-1]),vec[1][-1]+v*np.sin(teta[-1]),vec[2][-1]+w]);

def bruit(a,b,mu,sigma):
	for i in range(0,np.size(a)):
		b.append(a[i]+np.random.normal(mu,sigma));
	
def main():
    pass	

		
		

if (__name__ == '__main__'):
	main()
