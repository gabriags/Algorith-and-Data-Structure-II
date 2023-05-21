from algo1 import *
from mylinkedlist import *
from myqueue import *


#Clase de vertice
#Posee un valor, un color(blanco,gris o negro), una distancia(para BFS y DFS) y una lista de adyacencia
class vertex():
    value = None
    color = "white"
    ady = None
    d = 0
    pi = None
    children = None


#Clase para los arboles DFS y BFS
class FStree():
    root = None



#INPUT: Lista de vertices y Lista de Aristas
#Crea Lista de Adyacencia de un Grafo
#OUTPUT: Lista de Adyacencia
def createGraph(V,A):
    #Crea la estructura
    n = len(V)
    m = len(A)
    Graph = Array(n,vertex())

    #Agrega los vertices a Graph
    for i in range(0,n):
        newVertex = vertex()
        newVertex.value = V[i]
        newVertex.ady = LinkedList()
        Graph[i] = newVertex
    
    #Agrego las artistas a cada vertice
    for i in range(0,m):
        register = False
        for j in range(0,n):
            if Graph[j].value == A[i][0]:
                for k in range(0,n):
                    if Graph[k].value == A[i][1]:
                        add(Graph[j].ady,Graph[k])
                        add(Graph[k].ady,Graph[j])

    return Graph

#Realiza un recorrido por BFS
#Retorna un arbol BFS a partir de un vertice del grafo
def BFS(G,vert):
    
    vert.color = "gray"

    Q = LinkedList()
    BFST = FStree()

    enqueue(Q,vert)
    while Q.head!=None:

        u = dequeue(Q)
        u.children = LinkedList()

        if BFST.root == None:
            BFST.root = u

        #Recorro los nodos adyacentes, se agregan al arbol los no visitados
        currentNode = u.ady.head
        while currentNode!=None:
            if currentNode.value.color == "white":

                currentNode.value.color = "gray"
                currentNode.value.d = u.d +1
                currentNode.value.pi = u
                add(u.children,currentNode.value)

                enqueue(Q,currentNode.value)
            currentNode = currentNode.nextNode
        
        u.color = "black"

    return BFST


#Recorre el grafo por DFS  
def DFS(G):
    timed = -1
    n = len(G)
    for i in range(0,n):
        if G[i].color == "white":
            DFS_Visit(G,G[i],timed)

def DFS_Visit(G,u,timed):
    timed += 1
    u.d = timed
    u.color = "gray"
    currentNode = u.ady.head
    while currentNode!=None:
        if currentNode.value.color == "white":
            currentNode.value.pi = u
            DFS_Visit(G,currentNode.value,timed)
        currentNode = currentNode.nextNode
    u.color = "black"
    timed += 1
    u.f = timed

#Devuelve las propiedades de los vertices del grafo al inicio
def resetGraph(G):
    for i in range(0,len(G)):
        G[i].color="white"
        G[i].d=0
        G[i].children = None
        G[i].pi=None
    return G



#Imprime un grafo 
def printG(G):
    n = len(G)
    for i in range(0,n):
        currentNode = G[i].ady.head
        if currentNode!=None:
            print("vertice",G[i].value,': ',end='')
            while currentNode!=None:
                if currentNode.nextNode!=None:
                        print("[",currentNode.value.value,"] ➝ ",end="")
                else:
                    print("[",currentNode.value.value,"] ➝ ",currentNode.nextNode,"\n") 
                currentNode = currentNode.nextNode
        else:
            print("vertice",G[i].value,": ",currentNode,"\n")