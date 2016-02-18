import actualisation as actu
import mesures as me
import prediction as pre
import miseajour as maj
import initialisation as init 
from graphique import *
import sys
import pickle
import matplotlib.pyplot as plt

if len(sys.argv)>1:
   number=sys.argv[1]
else: 
    number=0
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
    addGraph(actu.vecKalman,True)
    addGraph([],False)#mesure absolue des ameres
    init.touslesamers()

    for i in range(500):
        #CalculerPositions():
        actu.actualisation(1,0.1)
        maj.MiseAjourEtat()
        print(actu.vecKalman[-1]) 
        #CalculerCapteurs()
        #print(mu.mesureAbsolueDesAmeres(actu.vec[-1],ameres))
        me.EtatMesure.append(me.mesureRelativeDesAmeres(actu.vec[-1],ameres))
        #Dessiner():
        setGraph(1,actu.vec)
        setGraph(2,actu.vecbruit)
        setGraph(3,actu.vecKalman)
        Xrobot=actu.vec[-1][0]
        Yrobot=actu.vec[-1][1]
        setGraph(4,me.mesureAbsolueDesAmeres(actu.vec[-1],ameres))
        graphDraw(Xrobot,Yrobot)

    plt.show()
    plt.pause(60)
