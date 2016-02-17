import actualisation as actu
from graphique import *
import sys
import pickle
import matplotlib.pyplot as plt


number=sys.argv[1]
Fichier=open('data'+str(number)+'.txt','rb')
ameres=pickle.load(Fichier)
Fichier.close()

Xrobot=0
Yrobot=0

if(__name__=="__main__"):
    plt.axis([-20, 20, -10, 30],'equal')
    actu.init(0,0,0)
    addGraph(ameres,False)
    addGraph(actu.vec,True)
    addGraph(actu.vecbruit,True)
    for i in range(500):
        #CalculerPositions():
        actu.actualisation(1,0.1)
        setGraph(1,actu.vec)
        setGraph(2,actu.vecbruit)
        Xrobot=actu.vec[-1][0]
        Yrobot=actu.vec[-1][1]
        #CalculerCapteurs()
        #Dessiner():
        graphDraw(Xrobot,Yrobot)
    plt.pause(60)
