import numpy as np 
import matplotlib.pyplot as pyplot
import actualisation as actu
import mesures as me
import miseajour as maj




def toMatrix(A):
	return np.transpose(np.asmatrix(A))

def Fxk():
        Uk=actu.u
        Xk=actu.vecKalman[-2]
	F = [0]*np.size(Xk);
	F[0] = [0]*np.size(Xk);
	F[0][0] = 1;
	F[1] = [0]*np.size(Xk);
	F[1][1] = 1;
	F[2] = [0]*np.size(Xk);
	F[2][2] = 1;
	F[2][0] = -Uk[0]*np.sin(Xk[3]);
	F[2][1] = Uk[0]*np.cos(Xk[3]);
	for i in range(3,np.size(Xk)):
		F[i] = [0]*np.size(Xk);
		F[i][i]=1;
	return toMatrix(F)

def Fuk():
        Xk=actu.vecKalman[-2]
	F = [0]*2;
	F[0] = [0]*np.size(Xk);
	F[1] = [0]*np.size(Xk);
	F[0][0] = np.cos(Xk[2]);
	F[0][1] = np.sin(Xk[2]);
	F[1][2] = 1;
	return toMatrix(F)


def Qk():
    	Xk=actu.vecKalman[-2]
        sigma_rho=me.sigmarho
        sigma_alpha=me.sigmaalpha
        F = Fuk();
	Q = [[sigma_rho,0],[0,sigma_alpha]];
	Q = np.asmatrix(Q);
	F_transpose = toMatrix(F);
	return np.transpose(F_transpose)*Q*F_transpose


def Pk():
        Pk_1=maj.MatricePkk[0]
        MFxk=Fxk()
        MQk=Qk()
        #print("d")
        #print(MFxk)
        #print(Pk_1)
        #print(MQk)
	return MFxk*Pk_1#*np.transpose(MFxk) + MQk

if __name__ == '__main__':
	pass


	
