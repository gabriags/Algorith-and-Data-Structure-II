#Direccionamiento abierto
import copy

class dictionaryNode():
    value = None
    key = None

def Dictionary(m):
    data = []
    data = [copy.deepcopy(None) for i in range(0,m)]
    return data

def printD(D):
    for i in range(0,len(D)):
        if D[i] != None:
            print(f'{i}[k:{D[i].key} v:{D[i].value}]')
        else:
            print(f'{i}[None]')

def insert(D,key,value):
    flag = False
    i = 0
    m = len(D)
    while flag == False:
        h = hash(key,i,m,3)  #Remplazar el ultimo argumento con 1:LP 2:QP 3:DH
        i +=1
        print(f'{key}+{i-1}= {h}')
        if D[h] == None:
            flag = True
    Node = dictionaryNode()
    Node.key = key
    Node.value = value
    D[h] = Node
    return D

def hash(k,i,m,method):
    h1 = k #Esto es h´(k)
    #Linear Probing
    if method == 1:
        return (h1 + i) % m
    #Quadratic Probing
    if method == 2:
        t0 = h1
        t1 = 1*i
        t2 = 3*(i**2)
        result = (t0 + t1 + t2) % m
        return result   #c1 = 1 y c2 = 3
    #Doble Hashing
    if method == 3:
        h1 = k
        h2 = 1 + (k%(m-1))
        result = (h1 +(i*h2))%m
        return result  
    
D = Dictionary(11)
printD(D)
insert(D,10,'a')
insert(D,22,'b')
insert(D,31,'c')
insert(D,4,'d')
insert(D,15,'e')
insert(D,28,'f')
insert(D,17,'g')
insert(D,88,'h')
insert(D,59,'h')


printD(D)