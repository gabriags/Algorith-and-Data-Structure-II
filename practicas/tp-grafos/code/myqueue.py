from mylinkedlist import *

def enqueue(Q,element):
    add(Q,element)

def dequeue(Q):
    if Q.head==None:
        return None
    else:
        currentNode=Q.head
        #caso de que solamente tenga elemento
        if currentNode.nextNode==None:
            element=currentNode.value
            Q.head=None
            return element
        else:
            #caso de que tenga mas de un elemento
            while currentNode!=None:
                if currentNode.nextNode.nextNode==None:
                    element=currentNode.nextNode.value
                    currentNode.nextNode=None
                    return element
                currentNode=currentNode.nextNode   