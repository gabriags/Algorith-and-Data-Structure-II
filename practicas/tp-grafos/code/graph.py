
from algo1 import *
from mylinkedlist import *
from myqueue import *


class vertex():
    value = None
    color = "white"
    d = 0
    f = 0
    pi = None
    ady = None


#Ejercicio 1
#Crea un grafo representandolo por lista de adyacencia
#Retorna el grafo
def createGraph(List_vertice,List_aristas):
    Graph = Array(length(List_vertice),vertex())

    #Inserta los vertices en el array
    currentNode = List_vertice.head
    for i in range(0,len(Graph)):
        Graph[i] = vertex()
        Graph[i].value = currentNode.value
        Graph[i].ady = LinkedList()
        currentNode = currentNode.nextNode
    
    #Inserta los adyacentes de cada vertice
    currentNode = List_aristas.head
    while currentNode.nextNode.nextNode!=None:
        insertGraph(Graph,currentNode.value,currentNode.nextNode.value)
        currentNode=currentNode.nextNode.nextNode
    insertGraph(Graph,currentNode.value,currentNode.nextNode.value)

    return Graph

#Inserta una arista entre verA y verB
#Utiliza lista de adyacencia
def insertGraph(Graph,verA,verB):
    n = len(Graph)
    for i in range(0,n):
        if Graph[i].value == verA:
            for j in range(0,n):
                if Graph[j].value == verB:
                    add(Graph[i].ady,Graph[j])
        if Graph[i].value == verB:
            for j in range(0,n):
                if Graph[j].value == verA:
                    add(Graph[i].ady,Graph[j])

#Elimina una arista entre verA y verB
#Utiliza lista de adyacencia
def deleteGraph(Graph,verA,verB):
    n = len(Graph)
    for i in range(0,n):
        if Graph[i].value == verA:
            for j in range(0,n):
                if Graph[j].value == verB:
                    delete(Graph[i].ady,Graph[j])
        if Graph[i].value == verB:
            for j in range(0,n):
                if Graph[j].value == verA:
                    delete(Graph[i].ady,Graph[j])


#Devuelve las propiedades de los vertices del grafo al inicio
def resetGraph(G):
    for i in range(0,len(G)):
        G[i].color="white"
        G[i].d=0
        G[i].f=0
        G[i].pi=None
    return G

#Ejercicio 2
#Determina si existe un camino entre dos vertices
#Utiliza DFS para encontrar un camino
#Devuelve True si existe y False si no
def existPath(G,v1,v2):
    v1.color = "gray"

    Q = LinkedList()

    enqueue(Q,v1)
    while Q.head!=None:
        u = dequeue(Q)
        currentNode = u.ady.head
        while currentNode!=None:
            if currentNode.value.color == "white":
                if currentNode.value == v2:
                    return True
                currentNode.value.color = "gray"
                enqueue(Q,currentNode.value)
            currentNode = currentNode.nextNode
        u.color = "black"
    return False



#Ejercicio 3
#Determina si un grafo es conexo o no
#Utiliza BFS para colorear de negro aquellos nodos conectados
def isConnected(G):
    BFS(G,G[0])
    n = len(G)
    count = 0
    for i in range(0,n):
        if G[i].color=="black":
            count +=1
    return count==n 

#Ejercicio 4
#Realiza un recorrido por BFS
#Si en algun momento el vertice que apunta tiene color gris
#Significa que existe un ciclo
#Si no posee ciclos entonces es un arbol
def isTree(G):
    G[0].color = "gray"
    
    Q = LinkedList()
    enqueue(Q,G[0])
    while Q.head!=None:
        u = dequeue(Q)
        currentNode = u.ady.head
        while currentNode!=None:
            if currentNode.value.color=="gray":
                return False
            elif currentNode.value.color == "white":
                currentNode.value.color="gray"
                enqueue(Q,currentNode.value)
            currentNode = currentNode.nextNode
        u.color = "black"
    return True

#Ejercicio 5
#Determina que aristas deben ser eliminadas para que
#el grafo se vuelva un árbol a partir de una raiz
#Retorna una lista con los pares de aristas
def ListToTree(G,vert):
    
    vert.color = "gray"
    Q = LinkedList()
    T = LinkedList()
    enqueue(Q,vert)
    while Q.head!=None:
        u = dequeue(Q)
        currentNode = u.ady.head
        while currentNode!=None:
            if currentNode.value.color=="gray":
                add(T,currentNode.value.value)
                add(T,u.value)
            elif currentNode.value.color == "white":
                currentNode.value.color="gray"
                enqueue(Q,currentNode.value)
            currentNode = currentNode.nextNode
        u.color = "black"
    return T


#Ejercicio 7
#Determina la cantidad de componentes conexos de un grafo
def countConnections(G):

    n= len(G) 
    count=0
    for i in range(0,n):
        if G[i].color=="white":
            count+=1
            BFS(G,G[i])
    return count  

#Ejercicio 8
#Convierte un grafo en un arbol
#Si no es conexo retorna el grafo original
def convertToTree(G,v):

    if isConnected(G)==False:
        return False

    G = resetGraph(G)
    #Determinamos si ya era un arbol
    if isTree(G)==False:
        G = resetGraph(G)
        #Determina las aristas que se deben eliminar
        T = ListToTree(G,v)
        #Inserta los adyacentes de cada vertice
        currentNode = T.head
        while currentNode.nextNode.nextNode!=None:
            deleteGraph(G,currentNode.value,currentNode.nextNode.value)
            currentNode=currentNode.nextNode.nextNode
        deleteGraph(G,currentNode.value,currentNode.nextNode.value) 

    return G    



#Recorre el grafo por BFS
def BFS(G,vert):
    
    vert.color = "gray"
    vert.d = 0
    

    Q = LinkedList()

    enqueue(Q,vert)
    while Q.head!=None:
        u = dequeue(Q)
        currentNode = u.ady.head
        while currentNode!=None:           
            if currentNode.value.color == "white":
                currentNode.value.color="gray"
                currentNode.value.d = u.d +1
                currentNode.value.pi = u
                enqueue(Q,currentNode.value)
            currentNode = currentNode.nextNode
        u.color = "black"

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