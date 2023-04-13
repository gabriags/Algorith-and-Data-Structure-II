from algo1 import *
from linkedlist import add
from linkedlist import delete as deleteLL

class dictionaryNode():
    key = None
    value = None
    nextNode = None

class dictionary():
    head = None

#Ejercicio 2
def Dictionary(m):
    return Array(m,dictionary())

#Insert
def insert(D,key,value):
    h = hash(key)
    if D[h]==None:
        L = dictionary()
        D[h] = L

    newNode = dictionaryNode()
    newNode.key = key
    newNode.value = value
    newNode.nextNode = D[h].head
    D[h].head = newNode
    return D
        

def hash(key):
    return key%9

#Search
def search(D,key):
    h = hash(key)
    currentNode = D[h].head
    while currentNode!=None:
        if currentNode.value==key:
            return key
        currentNode = currentNode.nextNode
    return None

#Delete
def delete(D,key):
    h = hash(key)
    #Caso 1: Posicion vacia
    if D[h] == None:
        return D
    else:
        currentNode = D[h].head
        #Caso 2: El key esta en la cabeza de la lista
        #Si sa vacia una lista se busca que el slot de el diccionario quede vacio
        if currentNode.key == key:
            if currentNode.nextNode == None:
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
