import numpy as np 
import matplotlib.pyplot as pyplot

def mesureExacte(vect,amer):
	ro = np.sqrt(np.power(vect[0]-amer[0],2)+np.power(vect[1]-amer[1],2));
	if vect[0]==amer[0]:
		return [ro,0]
	return  [ro,np.arctan2((vect[1]-amer[1])/(vect[0]-amer[0]))]

if __name__ == '__main__':
	v = mesureExacte([0,0],[1,0]);
	print(str(v[0])+" "+str(v[1]))