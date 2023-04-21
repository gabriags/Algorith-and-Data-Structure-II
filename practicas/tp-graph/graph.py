from algo1 import *
from mylinkedlist import *

#Clase grafo
#Crea una matriz de adyacencia para un grafo
#Utiliza linked list
#El formato de V es Vertices = [v1,v2,...]
#El formatp de A es Aristas = [[v2,v3],[v1,v2],...]
def createGraph(V,A):
    Graph = Array(len(V),LinkedList())

    for i in range(0,len(A)):
        v1 = A[i][0]
        print(v1)
        if Graph[v1] == None:
            List = LinkedList()
            add(List,A[i][1])
            Graph[v1] = List
        else:
            add(Graph[v1],A[i][1])
    return Graph


#Imprime un grafo
def printG(Graph):
    for i in range(0,len(Graph)):
        if Graph[i] != None:
            print(f'vertice {i}', end=" ")
            printL(Graph[i])
        else:
            print(f'vertice {i} [{None}]')

