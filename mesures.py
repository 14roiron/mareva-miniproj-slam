import numpy as np 
import matplotlib.pyplot as pyplot

def mesureExacte(vect,amer):
	v = [];
	ro = np.sqrt(np.power(vect[0]-amer[0],2)+np.power(vect[1]-amer[1],2));
	v=[ro,np.arctan2((vect[1]+amer[1]),(vect[0]+amer[0]))*180/np.pi];
	return v

def mesureBruites(vect,amer):
	v = [];
	ro = bruit(np.sqrt(np.power(vect[0]-amer[0],2)+np.power(vect[1]-amer[1],2)),0,0.5);
	v=bruit([ro,np.arctan2((vect[1]+amer[1]),(vect[0]+amer[0]))*180/np.pi],0,0.5);
	return v

def bruit(a,mu,sigma):
	return a+np.random.normal(mu,sigma);

if __name__ == '__main__':
	pass