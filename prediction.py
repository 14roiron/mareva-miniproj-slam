import numpy as np 
import matplotlib.pyplot as pyplot

def toMatrix(A):
	return np.transpose(np.asmatrix(A))

def Fxk(Xk,Uk):
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
	return F

def Fuk(Xk):
	F = [0]*2;
	F[0] = [0]*np.size(Xk);
	F[1] = [0]*np.size(Xk);
	F[0][0] = np.cos(Xk[2]);
	F[0][1] = np.sin(Xk[2]);
	F[1][2] = 1;
	return F


def Qk(Xk,sigma_rho,sigma_alpha):
	F = Fuk(Xk);
	Q = [[sigma_rho,0],[0,sigma_alpha]];
	Q = np.asmatrix(Q);
	F_transpose = np.asmatrix(F);
	return np.transpose(F_transpose)*Q*F_transpose


def Pk(Pk_1,Fxk,Qk):
	F = toMatrix(Fxk);
	return F*toMatrix(Pk_1)*np.transpose(F) + Qk

if __name__ == '__main__':
	pass


	