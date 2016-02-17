import actualisation
from graphique import *
import sys
import pickle
import matplotlib.pyplot as plt


number=sys.argv[1]
Fichier=open('data'+str(number)+'.txt','rb')
ameres=pickle.load(Fichier)
Fichier.close()

deplacement_global=[]


if(__name__=="__main__"):
    plt.axis([0, 20, 0, 20])
    addGraph(ameres,False)
    addGraph([],True)
    for i in range(500):
        #CalculerPositions()
        #CalculerCapteurs()
        #Dessiner():
            graphDraw()
    pass
    
