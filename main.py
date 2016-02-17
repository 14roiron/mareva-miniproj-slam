import actualisation
import graphique
import sys
import pickle



number=sys.argv[1]
Fichier=open('data'+str(number)+'.txt','rb')
ameres=pickle.load(Fichier)
Fichier.close()

deplacement_global=[]


if(__name__=="__main__"):
    #CalculerPositions()
    #CalculerCapteurs()
    #Dessiner()
    pass
    
