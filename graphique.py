import matplotlib.pyplot as plt


listGraphs=[]

def addGraph(listePoints,liee):
    listGraphs.append([])#on a un tableau par graph qui contient deux tableaux, pts en x et en y
    listGraphs[-1].append([])#x
    listGraphs[-1].append([])#y
    listGraphs[-1].append(liee)
    
    for (x,y) in listePoints:
        listGraphs[-1][0].append(x)
        listGraphs[-1][1].append(y)
        
        


def draw():
colors=0;
    style=0;
    colorTab=['r','b','g','y']
    plt.axis([0, 20, 0, 20])
    for graph in listGraphs():
        if graph[2]:
            lines = plt.plot(graph[0],graph[1])
            plt.setp(lines, color='r', linewidth=2.0) 
    plt.show()



if __name__=="__main__":
    plt.plot([1,2,3,4])
