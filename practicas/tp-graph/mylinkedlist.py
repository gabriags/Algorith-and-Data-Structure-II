class LinkedList():
    head=None

class Node():
    value=None
    nextNode=None



#Añade nodos a una variable del tipo Node
#Complejidad O(1)
def add(L,element):
    nodeA=Node()
    nodeA.value=element
    nodeA.nextNode=L.head
    L.head=nodeA    


#Busca la primera instancia de un elemento en un Linkedlist
#Devuelve la posicion donde se encuentra el elemento
#Complejidad O(n)
def search(L,element):
    currentNode=L.head
    if L.head==None:
        return None
    else:
        count=0
        while currentNode!=None:
            if currentNode.value==element:
                return count
            else:
                count+=1
                currentNode=currentNode.nextNode
        return None                        


#Inserta un elemento en un posiciond definida de una LinkedList
#Devuelve la posicion donde se inserto
#Orden de complejidad O(n)
def insert(L,element,position):
    if L.head==None and position==0:
        add(L,element)
        return position
    else:
        currentNode=L.head
        count=0
        while currentNode!=None:
            if count==position-1:
                newNode=Node()
                newNode.value=element
                newNode.nextNode=currentNode.nextNode
                currentNode.nextNode=newNode
                return position
            count+=1
            currentNode=currentNode.nextNode
        return None


#Elimina la primera instancia de un elemento en una LinkedList
#Devuelve la posicion donde se elimino
#Orden de complejidad O(n)
def delete(L,element):
    currentNode=L.head
    position=0
    if currentNode!=None:
        #Caso elemento en el primer nodo
        currentNode=L.head
        if currentNode.value==element:
            L.head=currentNode.nextNode
            return position
        elif currentNode.nextNode!=None:
            #Condiciona las listas de un unico nodo
            while currentNode!=None:
                if currentNode.nextNode.value==element:
                    currentNode.nextNode=currentNode.nextNode.nextNode
                    return position+1       
                currentNode=currentNode.nextNode
                position+=1
        return None

#Calcula la cantidad de nodos de una Linked List
#Devuelve el tamaño de la Linked List
#Orden de complejidad O(n)
def length(L):
    currentNode=L.head
    count=0
    while currentNode!=None:
        count=count+1
        currentNode=currentNode.nextNode
    return count


#Accede a un elemento en la posicion determinada de una Linked List
#Devuelve el elemento en la posicion
#Orden de complejidad O(n)
def access(L,position):
    currentNode=L.head
    if currentNode==None:
        return None
    else:
        count=0
        while currentNode!=None:
            if count==position:
                return currentNode.value
            count+=1    
            currentNode=currentNode.nextNode
        return None                                

#Actualiza el elemento en la posicion determinada
#Devuelve la posicion donde se actualizo el elemento
#Orden de complejidad O(n)
def update(L,element,position):
    currentNode=L.head
    if currentNode==None:
        return None
    else:
        count=0
        while currentNode!=None:
            if count==position:
                currentNode.value=element
                return position
            count+=1    
            currentNode=currentNode.nextNode
        return None                                


#Imprime la Linked list deseada
def printL(L):
    
    currentNode=L.head
    print(' [',end='')
    while currentNode!=None:
        if currentNode.nextNode!=None:
            print(currentNode.value,", ",end="")
        else:
            print(currentNode.value,"]")    
        currentNode=currentNode.nextNode      

#Invierte una lista enlazada
def reverse(L):
    pre = next = None
    currentNode=L.head
    while currentNode!=None:
        next = currentNode.nextNode
        currentNode.nextNode = pre
        pre = currentNode
        currentNode = next
    L.head = pre


