from algo1 import *
from linkedlist import add
from linkedlist import delete as deleteLL

class dictionaryNode():
    key = None
    value = None
    nextNode = None

class dictionary():
    head = None

#Defino el diccionario como un Array de nodos dictionary
def Dictionary(m):
    return Array(m,dictionary())

#Insert
#Inserta un value a través de una key en un diccionario D
#Devuelve el diccionario con la insercion
#Las colisiones se resuelven por encadenamiento
def insert(D,key,value):
    h = hash(key,len(D))
    if D[h]==None:
        L = dictionary()
        D[h] = L

    newNode = dictionaryNode()
    newNode.key = key
    newNode.value = value
    newNode.nextNode = D[h].head
    D[h].head = newNode
    return D
        
#Utilizo una llave y un modulo para aplicar metodo de la division
#Segun el tipo de dato(numerico,caracter o string) aplica diferentes calculos
def hash(key,module):
    if type(key)==int:
        return key % module
    elif type(key)==str:
        n = len(key)
        for i in range(0,n):
            if i==0:
                j = n-1
                newkey = ord(key[i])*(255**j)
            else:
                j -= 1
                newkey += ord(key[i])*(255**j)
        return newkey % module
    
#Search
#Busca la key en el diccionario D
#Devuelve el value asociado a la key o None si no lo encuentra
def search(D,key):
    h = hash(key,len(D))
    if D[h] == None:
        return None
    currentNode = D[h].head
    while currentNode!=None:
        if currentNode.key==key:
            return currentNode.value
        currentNode = currentNode.nextNode
    return None

#Delete
#Elimina una Key en un diccionario D
#Devuelve el diccionario
def delete(D,key):
    h = hash(key,len(D))
    #Caso 1: Posicion vacia
    if D[h] == None:
        return D
    else:
        currentNode = D[h].head
        #Caso 2: El key esta en la cabeza de la lista
        #Si sa vacia una lista se busca que el slot de el diccionario quede vacio
        if currentNode.key == key and currentNode.nextNode == None:
            D[h] = None
        #Caso 3: Hay colisiones en la posicion
        else:
            currentNode=D[h].head
            #Caso elemento en el primer nodo
            if currentNode.key==key:

                D[h].head=currentNode.nextNode
            elif currentNode.nextNode!=None:
                flag = True
                while currentNode!=None and flag:
                    if currentNode.nextNode==None:
                        flag = False
                    elif currentNode.nextNode.key==key:
                        currentNode.nextNode=currentNode.nextNode.nextNode
                        flag = False
                    currentNode=currentNode.nextNode
        return D

#Actualiza el value de un nodo en un dictionary
def update(D,key,value):
    m = len(D)
    currentNode = D[hash(key,m)]
    if currentNode==None:
        return None
    else:
        currentNode = currentNode.head
        while currentNode!=None:
            if currentNode.key == key:
                currentNode.value = value
                return value
            currentNode = currentNode.nextNode
        return None

    
#Imprime una lista de colisiones en un diccionario
def printD(D):
    for i in range(len(D)):
        print(f'{i}:',end=" ")
        if D[i] == None:
            print(D[i])
        else:
            currentNode=D[i].head
            print(' [',end='')
            while currentNode!=None:
                if currentNode.nextNode!=None:
                    print(f"k:{currentNode.key} v:{currentNode.value}| ",end="")
                else:
                    print(f"k:{currentNode.key} v:{currentNode.value}]")    
                currentNode=currentNode.nextNode      
