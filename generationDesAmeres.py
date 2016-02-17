import sys
import pickle
from random import randint


number=sys.argv[1]
l=[]
for i in range(1):
    l.append([randint(-15,15),randint(-5,25)])
print(l)
Fichier = open('data'+str(number)+'.txt','wb')
pickle.dump(l,Fichier) 
Fichier.close()
