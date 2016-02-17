import numpy as np 
import matplotlib.pyplot as pyplot

EtatMesure=[]

def mesureRelativeDesAmeres(VecteurEtat,amers):
    liste=[]
    for amer in amers:
        liste.append(mesureExacte(VecteurEtat,amer))
    return liste

def mesureAbsolueDesAmeres(VecteurEtat,amers):
    liste=mesureRelativeDesAmeres(VecteurEtat,amers)
    retour=[]
    for (ro,theta) in liste:
        x=VecteurEtat[0]+ro*np.cos(VecteurEtat[2]+theta)
        y=VecteurEtat[1]+ro*np.sin(VecteurEtat[2]+theta)
        retour.append([x,y])
    return retour    

def mesureExacte(vect,amer):
	v = [];
	ro = np.sqrt(np.power(vect[0]-amer[0],2)+np.power(vect[1]-amer[1],2));
	v=[ro,vec[2]-np.arctan2((vect[1]+amer[1]),(vect[0]+amer[0]))*180/np.pi];
	if ro>=4:
		ro=-1;
	if v[1]>=60 or v[1]<=-60:
		ro=-1;
	return v

def mesureBruites(vect,amer):
	v = [];
	ro = bruit(np.sqrt(np.power(vect[0]-amer[0],2)+np.power(vect[1]-amer[1],2)),0,0.5);
	v=[ro,bruit(vec[2]-np.arctan2((vect[1]+amer[1]),(vect[0]+amer[0])),0,0.5)];
	if ro>=4:
		ro=-1;
	if v[1]>=60 or v[1]<=-60:
		ro=-1;
	return v

def bruit(a,mu,sigma):
	return a+np.random.normal(mu,sigma);

if __name__ == '__main__':
	pass
