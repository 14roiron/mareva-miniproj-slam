import numpy as np 
import matplotlib.pyplot as pyplot
import mesures as me
import main as m
vec = [];
vecbruit = [];
vecKalman=[]


u=[0,0]

def init(x0,y0,teta0):
	vec.append([x0,y0,teta0]);
	vecbruit.append([x0,y0,teta0]);
        vecKalman.append(vec[0]+ me.mesureRelativeDesAmeres(vec[0],m.ameres))
        
def actualisation(v,w):
        u=[v,w]
	vecbruit.append([vecbruit[-1][0]+bruit(v,0,0.1)*np.cos(vecbruit[-1][2]),vecbruit[-1][1]+bruit(v,0,0.1)*np.sin(vecbruit[-1][2]),vecbruit[-1][2]+bruit(w,0,0.1)]);
	vec.append([vec[-1][0]+v*np.cos(vec[-1][2]),vec[-1][1]+v*np.sin(vec[-1][2]),vec[-1][2]+w]);
        vecKalman.append([])
def bruit(a,mu,sigma):
	return a+np.random.normal(mu,sigma);
	
def main():
    pass	

		

if (__name__ == '__main__'):
	main()
