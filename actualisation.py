import numpy as np 
import matplotlib.pyplot as pyplot
import mesures as me
import main as m
vec = [];
vecbruit = [];
vecKalman=[]

sigmav=0.1
sigmaw=0.05
u=[0,0]
ub=[0,0]

def init(x0,y0,teta0):
	vec.append([x0,y0,teta0]);
	vecbruit.append([x0,y0,teta0]);
        vecKalman.append(vec[0]+ me.mesureRelativeDesAmeres(vec[0],m.ameres))
def actualisation(v,w):
	global u,ub
	u=[v,w]
	ub=consignebruite(u)
	vecbruit.append([vecbruit[-1][0]+ub[0]*np.cos(vecbruit[-1][2]),vecbruit[-1][1]+ub[0]*np.sin(vecbruit[-1][2]),vecbruit[-1][2]+ub[1]]);
	vec.append([vec[-1][0]+v*np.cos(vec[-1][2]),vec[-1][1]+v*np.sin(vec[-1][2]),vec[-1][2]+w]);
	vecKalman.append([])
def bruit(a,mu,sigma):
	return a+np.random.normal(mu,sigma);

def consignebruite(u):
    return [bruit(u[0],0,sigmav),bruit(u[1],0,sigmaw)]

def actu_kalman(Xk):
	pos= [Xk[-2][0]+ub[0]*np.cos(Xk[-2][2]),Xk[-2][1]+ub[0]*np.sin(Xk[-2][2]),Xk[-2][2]+ub[1]];
	retour=list(Xk[-2])
	for i in range(3):
		retour[i]=pos[i]
	return retour


def main():
    pass	

		

if (__name__ == '__main__'):
	main()
