import numpy as np 
import matplotlib.pyplot as pyplot

def mesureExacte(vect,amer):
	v = [];
	ro = np.sqrt(np.power(vect[0]-amer[0],2)+np.power(vect[1]-amer[1],2));
	v=[ro,np.arctan2((vect[1]+amer[1]),(vect[0]+amer[0]))*180/np.pi];
	return v

if __name__ == '__main__':
	v =[];
	v = mesureExacte([0,0],[-1,1]);
	print(str(v[0])+" "+str(v[1]))