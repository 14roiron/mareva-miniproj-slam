import numpy as np
import prediction as pre
import mesures as me
import actualisation as actu









def MatriceHk(Xk,Ameres):
    taille=np.size(Xk)+np.size(Ameres)
    matrice=[]
    matrice.append([])
    xk=Xk[0]
    yk=Xk[1]
    for i in range(np.size(Ameres)):
       matrice[-1].append((-xk)/(2*np.sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
       matrice[-1].append(((Ameres[i][1]-yk)/(Ameres[i][0]-xk)**2)/(1+((Ameres[i][1]-yk)/(Ameres[i][0]-xk))**2))

    matrice.append([])
    for i in range(np.size(Ameres)):
       matrice[-1].append((-yk)/(2*np.sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
       matrice[-1].append((1/(Ameres[i][0]-xk))/(1+((Ameres[i][1]-yk)/(Ameres[i][0]-xk))**2))

    matrice.append([])
    for i in range(np.size(Ameres)):
        matrice[-1].append(0)
        matrice[-1].append(1)


    for i in range(np.size(Ameres)):
        matrice.append(np.size(Ameres)*2*[0])
        matrice.append(np.size(Ameres)*2*[0])
    for i in range(np.size(Ameres)):
        indiceX=3+2*i
        indiceY=2*i
        matrice[indiceX][indiceY]=((xk)/(2*np.sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
        matrice[indiceX][indiceY+1]=-(((Ameres[i][1]-yk)/(Ameres[i][0]-xk)**2)/(1+((Ameres[i][1]-yk)/(Ameres[i][0]-xk))**2))

        matrice[indiceX+1][indiceY]=((yk)/(2*np.sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
        matrice[indiceX+1][indiceY+1]=-((1/(Ameres[i][0]-xk))/(1+((Ameres[i][1]-yk)/(Ameres[i][0]-xk))**2))

    return pre.toMatrix(matrice)   

def MatriceYk(Xk)
    return me.mesureRelativeDesAmeres(actu.)



def MatriceRk(Ameres):
    matrice=[]
    for i in range(2*np.size(Ameres)):
        matrice.append(2*np.size(Ameres)*[0])
    for i in range(np.size(Ameres)):
        matrice[2*i][2*i]=me.sigmarho
        matrice[2*i+1][2*i+1]=me.sigmaalpha
    return pre.toMatrix(matrice)
