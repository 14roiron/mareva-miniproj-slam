import numpy as np
import mesures as me
import prediction as pre
import actualisation as actu
import main as m
import miseajour as maj


def touslesamers():
        sigmaalpha=me.sigmaalpha
	sigmarho=me.sigmarho
        Z0=me.mesureRelativeDesAmeres(actu.vec[0],m.ameres)
	P = [0.]*(3+np.size(Z0));
	for i in range(0,3+np.size(Z0)):
		P[i] = [0.]*(3+np.size(Z0));
	P = pre.toMatrix(P);
	J = [0.]*(np.size(Z0)/2);
	R = pre.toMatrix([[np.power(sigmarho,2) , 0],[0 , np.power(sigmaalpha,2)]]);
	for i in range(0,np.size(Z0)/2):
		J[i] = pre.toMatrix([[np.cos(Z0[2*i+1]) , np.sin(Z0[2*i+1])],[-Z0[2*i]*np.sin(Z0[2*i+1]) , Z0[2*i]*np.cos(Z0[2*i+1])]]);
		Q = J[i]*R*np.transpose(J[i]);
		P[3+i,3+i] = Q[0,0];
		P[3+i,4+i] = Q[0,1];
		P[4+i,3+i] = Q[1,0];
		P[4+i,4+i] = Q[1,1];
        maj.MatricePk[0]=P

if __name__ == '__main__':
	pass
