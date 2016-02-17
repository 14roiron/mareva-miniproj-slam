import numpy as np 
import matplotlib.pyplot as pyplot

x = [];
xbruit = [];
y = [];
teta = [];
v=1;
w=0.1;

def init(x0,y0,teta0):
	x.append(x0);
	y.append(y0);
	teta.append(teta0);

def actualisation(v,w):
	global x;
	global teta;
	global y;
	x.append(x[-1]+v*np.cos(teta[-1]));
	y.append(y[-1]+v*np.sin(teta[-1]));
	teta.append(teta[-1]+w);

def bruit(a,b,mu,sigma):
	for i in range(0,np.size(a)):
		b[i]= a[i]+np.random.normal(mu,sigma);
	
def main():
	global x;
	init(0,0,0);
	i=0;
	while i<100 :
		actualisation(v,w); i=i+1;
	bruit(x,xbruit,0,2);
	figure = pyplot.plot(x,y);
	figure = pyplot.sub_plot(xbruit,y);
	pyplot.show(figure);

		
		

if (__name__ == '__main__'):
	main()