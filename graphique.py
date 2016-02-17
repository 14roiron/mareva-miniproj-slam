import matplotlib.pyplot as plt

import numpy as np

plt.ion();
listGraphs=[]
robot=plt.scatter(0,0, s=8, c='purple', alpha=0.5)

def getListGraphs():
    return listGraphs


def addGraph(listePoints,liee):
    listGraphs.append([])#on a un tableau par graph qui contient deux tableaux, pts en x et en y
    listGraphs[-1].append([])#x
    listGraphs[-1].append([])#y
    listGraphs[-1].append(liee)
    listGraphs[-1].append(None)
    for pt in listePoints:
        listGraphs[-1][0].append(pt[0])
        listGraphs[-1][1].append(pt[1])
def setGraph(indice,liste):
    listGraphs[indice][0]=[]
    listGraphs[indice][1]=[]
    for pt in liste:
        listGraphs[indice][0].append(pt[0])
        listGraphs[indice][1].append(pt[1])



def graphDraw(Xrobot,Yrobot):
    global robot
    colors=0;
    style=0;
    colorTab=['r','b','g','y']
    styleTab=['+',',','.','1','2','3','4'];
    robot.remove()
    robot=plt.scatter(Xrobot,Yrobot, s=15, c='purple', alpha=0.5)
    for graph in listGraphs:
        if graph[3] is None:
            if graph[2]:
                graph[3] = plt.plot(graph[0],graph[1])[0]
                plt.setp(graph[3], color=colorTab[colors], linewidth=0.5) 
                colors+=1
            else:
                graph[3] = plt.plot(graph[0], graph[1], str(colorTab[colors]+styleTab[style]))[0]
                colors+=1
                style+=1
        else:
            graph[3].set_data(graph[0],graph[1])
    plt.draw()
    plt.pause(0.01)

if __name__=="__main__":
    a=[[1,2],[2,4],[8,10]]
    #plt.show()
    #fig = plt.figure()
    #ax = fig.add_subplot(1,1,1)
    plt.axis([-20, 20,-10, 30],'equal')
    b=[]
    addGraph(a,False)
    addGraph(b,True)
    for i in range(1500):
        b.append([i/100.,i*3/100.])
        setGraph(1,b)
        graphDraw()


    plt.pause(60)

