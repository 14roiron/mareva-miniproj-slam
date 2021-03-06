import numpy as np
import prediction as pre
import mesures as me
import actualisation as actu
import main as m
import numpy as np




MatricePkk=[[],[]]
MatricePk=[]


def MatriceHk():
    Xk=actu.vecKalman[-2]
    Ameres=m.ameres
    taille=len(Xk)+len(Ameres)
    matrice=[]
    matrice.append([])
    xk=Xk[0]
    yk=Xk[1]
    for i in range(len(Ameres)):
       matrice[-1].append((xk-Ameres[i][0])/(np.sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
       #matrice[-1].append(((Ameres[i][1]-yk)/(Ameres[i][0]-xk)**2)/(1+((Ameres[i][1]-yk)/(Ameres[i][0]-xk))**2))
       matrice[-1].append((Ameres[i][1]-yk)/(((Ameres[i][0]-xk)**2)+((Ameres[i][1]-yk)**2)))
    matrice.append([])
    for i in range(len(Ameres)):
       matrice[-1].append((yk-Ameres[i][1])/(np.sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
       #matrice[-1].append((1/(Ameres[i][0]-xk))/(1+((Ameres[i][1]-yk)/(Ameres[i][0]-xk))**2))
       matrice[-1].append(-(Ameres[i][0]-xk)/(((Ameres[i][0]-xk)**2)+((Ameres[i][1]-yk)**2)))
    matrice.append([])
    for i in range(len(Ameres)):
        matrice[-1].append(0)
        matrice[-1].append(-1)


    for i in range(len(Ameres)):
        matrice.append(len(Ameres)*2*[0])
        matrice.append(len(Ameres)*2*[0])
    for i in range(len(Ameres)):
        indiceX=3+2*i
        indiceY=2*i
        matrice[indiceX][indiceY]=((xk-Ameres[i][0])/(np.sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2)))
        matrice[indiceX][indiceY+1]=-((Ameres[i][1]-yk)/(((Ameres[i][0]-xk)**2)+((Ameres[i][1]-yk)**2)))

        matrice[indiceX+1][indiceY]=(yk-Ameres[i][1])/(np.sqrt((xk-Ameres[i][0])**2+(yk-Ameres[i][1])**2))
        matrice[indiceX+1][indiceY+1]=(Ameres[i][0]-xk)/(((Ameres[i][0]-xk)**2)+((Ameres[i][1]-yk)**2))

    return pre.toMatrix(matrice)   



def MatriceRk():
    Ameres=m.ameres
    matrice=[]
    for i in range(2*len(Ameres)):
        matrice.append(2*len(Ameres)*[0])
    for i in range(len(Ameres)):
        matrice[2*i][2*i]=me.sigmarho**2
        matrice[2*i+1][2*i+1]=me.sigmaalpha**2
    return pre.toMatrix(matrice)

def MatriceYk():
    T = [0]*2*len(m.ameres)
    for i in range(2*(len(m.ameres)-1)):
        T[i] = actu.vecKalman[-2][3+i]
   
    A = me.mesureRelativeDesAmeres(actu.vec[-1],m.ameres)
    B = me.h(actu.actu_kalman(actu.vecKalman),m.ameres)
    Y = [0]*len(A)
    for i in range(len(A)):
        Y [i] = A[i] - B[i]
#        print("ameres")
#       print(A[i])
#        print("B")
#        print(B[i])
    for i in range(len(Y)/2):
        Y[2*i+1] = me.modulopi(Y[2*i+1])
    Y = pre.toMatrix(Y)
    return Y


def MatriceSk():
    return MatriceHk()*pre.Pk()*np.transpose(MatriceHk())+MatriceRk()

def MatriceKk():
    return pre.Pk()*np.transpose(MatriceHk())*np.linalg.inv(MatriceSk())

def nptolist(matrice):
    array=matrice.tolist()
    for i in range(len(array)):
        array[i]=array[i][0]
    return array


def MiseAjourEtat():
    MatricePk=pre.Pk()
#   print("zk")
#   print(pre.toMatrix(me.mesureRelativeDesAmeres(actu.vec[-1],m.ameres)))
#   print("yk")
#   print(MatriceYk())
#    print("Xk-1")
#   print(actu.actu_kalman(actu.vecKalman))
#    print("K")
#    print(MatriceKk())
#    print("y")
#    print(MatriceYk())
    actu.vecKalman[-1]=nptolist(pre.toMatrix(actu.actu_kalman(actu.vecKalman))+MatriceKk()*MatriceYk());
    MatricePkk[1]=(np.identity(3+2*len(m.ameres))-MatriceKk()*MatriceHk())*pre.Pk()
    MatricePkk[0]=MatricePkk[1]

if __name__=="__main__":
    MiseAjourEtat()
