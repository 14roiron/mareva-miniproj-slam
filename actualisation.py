import numpy as np 
import matplotlib.pyplot as pyplot


vec = [];
vecbruit = [];

def init(x0,y0,teta0):
	vec.append([x0,y0,teta0]);
	vecbruit.append([x0,y0,teta0]);

def actualisation(v,w):
	global vec;
	vecbruit.append([vec[0][-1]+bruit(v,0,0.5)*np.cos(teta[-1]),vec[1][-1]+bruit(v,0,0.5)*np.sin(teta[-1]),vec[2][-1]+bruit(w,0,0.5)]);
	vec.append([vec[0][-1]+v*np.cos(teta[-1]),vec[1][-1]+v*np.sin(teta[-1]),vec[2][-1]+w]);

def bruit(a,mu,sigma):
	return a+np.random.normal(mu,sigma);
	
def main():
	pass

		

if (__name__ == '__main__'):
	main()
