import numpy as np



def MatriceHk(Xk,Ameres):
    taille=len(Xk)+len(Ameres)
    matrice=[]
    matrice.append([])
    xk=Xk[0]
    yk=Xk[1]
    for i in range(len(Ameres)):
       matrice[-1].append((-xk)/(2*sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
       matrice[-1].append(((Ameres[i][1]-yk)/(Ameres[i][0]-xk)**2)/(1+((Ameres[1]-yk)/(Ameres[0]-xk))**2))

    matrice.append([])
    for i in range(len(Ameres)):
       matrice[-1].append((-yk)/(2*sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
       matrice[-1].append((1/(Ameres[i][0]-xk))/(1+((Ameres[1]-yk)/(Ameres[0]-xk))**2))

    matrice.append([])
    for i in range(len(Ameres)):
        matrice[-1].append(0)
        matrice[-1].append(0)


    for i in range(len(Ameres)):
        matrice.append(len(Ameres)*2*[0])
        matrice.append(len(Ameres)*2*[0])
    for i in range(len(Ameres)):
        indiceX=3+2*i
        indiceY=2*i
        matrice[indiceX][indiceY]=((-xk)/(2*sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
        matrice[indiceX][indiceY+1]=-(((Ameres[i][1]-yk)/(Ameres[i][0]-xk)**2)/(1+((Ameres[1]-yk)/(Ameres[0]-xk))**2))

        matrice[indiceX+1][indiceY]=((-yk)/(2*sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
        matrice[indiceX+1][indiceY+1]=((1/(Ameres[i][0]-xk))/(1+((Ameres[1]-yk)/(Ameres[0]-xk))**2))
