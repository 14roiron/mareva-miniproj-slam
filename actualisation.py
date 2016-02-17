import numpy as np 
import matplotlib.pyplot as pyplot


vec = [];
vecbruit = [];

def init(x0,y0,teta0):
	vec.append([x0,y0,teta0]);
	vecbruit.append([x0,y0,teta0]);

def actualisation(v,w):
	global vec;
	vecbruit.append([vec[-1][0]+bruit(v,0,0.5)*np.cos(vec[-1][2]),vec[-1][1]+bruit(v,0,0.5)*np.sin(vec[-1][2]),vec[-1][2]+bruit(w,0,0.5)]);
	vec.append([vec[-1][0]+v*np.cos(vec[-1][2]),vec[-1][1]+v*np.sin(vec[-1][2]),vec[-1][2]+w]);

def bruit(a,mu,sigma):
	return a+np.random.normal(mu,sigma);
	
def main():
	pass

		

if (__name__ == '__main__'):
	main()
