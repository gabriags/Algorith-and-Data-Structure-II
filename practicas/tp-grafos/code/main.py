from graphnew import *



#Ejemplo de Grafo en las diapositivas de DFS y BFS
Vertices = ['R','S','T','U','V','W','X','Y']
Aristas = [['R','V'],['R','S'],['S','W'],['W','T'],['W','X'],['T','X'],['T','U'],['U','X'],['U','Y'],['X','Y']]


G = createGraph(Vertices,Aristas)
printG(G)