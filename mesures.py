import numpy as np 
import matplotlib.pyplot as pyplot

EtatMesure=[]
sigmarho=0.005
sigmaalpha=0.03
def mesureRelativeDesAmeres(VecteurEtat,amers):
    liste=[]
    for amer in amers:
        mesure=(mesureExacte(VecteurEtat,amer))
        liste.append(mesure[0])
        liste.append(mesure[1])
    return liste

def mesureAbsolueDesAmeres(VecteurEtat,amers):
    liste=mesureRelativeDesAmeres(VecteurEtat,amers)
    retour=[]
    for i in range(len(liste)/2):
        ro=liste[2*i]
        theta=liste[2*i+1]
        if ro==-1:
            pass
        else:
            #print("polaire:"+str([ro,theta]))
            x=VecteurEtat[0]+ro*np.cos(VecteurEtat[2]+theta)
            y=VecteurEtat[1]+ro*np.sin(VecteurEtat[2]+theta)
            retour.append([x,y])
    return retour    

def mesureExacte(vect,amer):
	v = [];
	ro = np.sqrt(np.power(vect[0]-amer[0],2)+np.power(vect[1]-amer[1],2));
	v=[ro,-vect[2]+np.arctan2((-vect[1]+amer[1]),(-vect[0]+amer[0]))];
	if ro>=4:
		ro=-1;
	if v[1]>=60 or v[1]<=-60:
		ro=-1;
	return v

def mesureBruites(vect,amer):
	v = [];
	ro = bruit(np.sqrt(np.power(vect[0]-amer[0],2)+np.power(vect[1]-amer[1],2)),0,sigmarho);
	v=[ro,bruit(-vect[2]+np.arctan2((-vect[1]+amer[1]),(-vect[0]+amer[0])),0,sigmaalpha)];
	if ro>=4:
		ro=-1;
	if v[1]>=60 or v[1]<=-60:
		ro=-1;
	return v

def bruit(a,mu,sigma):
	return a+np.random.normal(mu,sigma);

def hi(Xk,A):
    return [np.sqrt( np.power(A[0]-Xk[0],2) + np.power(A[1]-Xk[1],2)) , -Xk[2]+np.arctan2((-Xk[1]+A[1]),(-Xk[0]+A[0]))]

def modulopi(angle):
    angle=angle%(np.pi)
    if angle>np.pi:
        angle-=2*np.pi
    if angle<-np.pi:
        angle+=2*np.pi
    return angle

def h(Xk , A):
    H = [0]*2*len(A);
    for i in range(len(A)):
        H[2*i]=hi(Xk,A[i])[0]
        H[2*i+1] = hi(Xk,A[i])[1]
    return H

if __name__ == '__main__':
	pass
