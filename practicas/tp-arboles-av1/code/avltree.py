from linkedlist import *


class AVLTree:
  root = None


class AVLNode:
  bf = None
  key = None
  value = None
  leftnode = None
  rightnode = None
  parent = None


#Ingresa un nodo de un arbol
#Calcula la altura del nodo
#Devuelve la altura
def search_h(currentNode):
  if currentNode == None:
    return 0
  elif currentNode.leftnode == None and currentNode.rightnode == None:
    return 0
  elif currentNode.leftnode != None and currentNode.rightnode != None:
    h_left = search_h(currentNode.leftnode) + 1
    h_right = search_h(currentNode.rightnode) + 1
    if h_left >= h_right:
      return h_left
    else:
      return h_right
  elif currentNode.leftnode == None and currentNode.rightnode != None:
    return search_h(currentNode.rightnode) + 1
  else:
    return search_h(currentNode.leftnode) + 1


#Realiza una rotaciòn a izquierda de un AVL
#nodeA es el nodo actual, nodoB es el hijo que rota y nodoC es el nieto que cambia de padre
def rotateLeft(Tree, avlnode):
  nodeA = avlnode
  nodeB = avlnode.rightnode
  if nodeB.leftnode != None:
    nodeC = nodeB.leftnode
    nodeC.parent = nodeA
  else:
    nodeC = None
  nodeA.rightnode = nodeC
  nodeB.parent = nodeA.parent
  nodeA.parent = nodeB
  nodeB.leftnode = nodeA
  if nodeA == Tree.root:
    Tree.root = nodeB
  return nodeB


#Realiza una rotación a derecha de un AVL
#nodeA es el nodo actual, nodoB es el hijo que rota y nodoC es el nieto que cambia de padre
def rotateRight(Tree, avlnode):
  nodeA = avlnode
  nodeB = avlnode.leftnode
  if nodeB.rightnode != None:
    nodeC = nodeB.rightnode
    nodeC.parent = nodeA
  else:
    nodeC = None
  nodeA.leftnode = nodeC
  nodeB.parent = nodeA.parent
  nodeA.parent = nodeB
  nodeB.rightnode = nodeA
  if nodeA == Tree.root:
    Tree.root = nodeB
  return nodeB


''' #Calcula el factor de balance de un AVL
#Recorre el arbol en preorden
def calculateBalance(AVLTree):
  if AVLTree.root == None:
    return None
  else:
    L = LinkedList()
    calculateBalanceR(L, AVLTree.root)
    reverse(L)
    return L


def calculateBalanceR(L, currentNode):
  currentNode.bf = search_h(currentNode.leftnode) - search_h(
    currentNode.rightnode)
  add(L, currentNode.bf)
  if currentNode.leftnode != None:
    calculateBalanceR(L, currentNode.leftnode)
  if currentNode.rightnode != None:
    calculateBalanceR(L, currentNode.rightnode) '''

#Ejercicio Nro 2
def calculateBalance(AVLTree):
  if AVLTree.root == None:
    return None
  else:
    L = LinkedList() 
    insert(L, AVLTree.root, 0)
    calculateBalanceR(L, L.head, 1)
    printL(L)
    return AVLTree


def calculateBalanceR(L, currentNode, position):
  currentNode.value.bf = search_h(currentNode.value.leftnode) - search_h(
    currentNode.value.rightnode)
  if currentNode.value.leftnode != None:
    insert(L, currentNode.value.leftnode, position)
    position += 1
  if currentNode.value.rightnode != None:
    insert(L, currentNode.value.rightnode, position)
    position += 1
  if currentNode.nextNode != None:
    calculateBalanceR(L, currentNode.nextNode, position)
  currentNode.value = f'|Node: {currentNode.value.value} bf: {currentNode.value.bf}|'



#  ------------------------------Operaciones Basicas------------------------------
#Inserta un nuevo nodo en un arbol AVL
def insertAVL(B, element, key):
  Node = AVLNode()
  Node.key = key
  Node.value = element
  if B.root == None:
    B.root = Node
  else:
    insertR(Node, B.root)


#Busca la posicion donde insertar un nodo
#Si la key ya existe devuelve un error
def insertR(newNode, currentNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      currentNode.rightnode = newNode
      newNode.parent = currentNode
      return newNode.key
    else:
      return insertR(newNode, currentNode.rightnode)
  elif newNode.key < currentNode.key:
    if currentNode.leftnode == None:
      currentNode.leftnode = newNode
      newNode.parent = currentNode
      return newNode.key
    else:
      return insertR(newNode, currentNode.leftnode)
  else:
    return None


#Busca la primera instancia de un elemento en un arbol AVL
#Si lo encuentra devuelve la Key sino devuelve None
def searchAVL(B, element):
  if B.root == None:
    return None
  else:
    return searchAVLR(B.root, element)


def searchAVLR(currentNode, element):
  if currentNode.value == element:
    return currentNode.key
  else:
    if currentNode.leftnode != None:
      Left = searchAVLR(currentNode.leftnode, element)
      if Left != None:
        return Left
    if currentNode.rightnode != None:
      Right = searchAVLR(currentNode.rightnode, element)
      if Right != None:
        return Right


#Elimina la primera instancia de un elemento
def deleteAVL(B, element):
  if B.root == None:
    return None
  else:
    return deleteR(B, B.root, element)


def deleteR(B, currentNode, element):
  if currentNode.value == element:
    return delete_nodeAVL(B, currentNode)
  else:
    if currentNode.leftnode != None:
      Left = deleteR(B, currentNode.leftnode, element)
      if Left != None:
        return Left
    if currentNode.rightnode != None:
      Right = deleteR(B, currentNode.rightnode, element)
      if Right != None:
        return Right


def delete_nodeAVL(B, currentNode):
  #Prime caso: nodo sin hijos
  if currentNode.leftnode == None and currentNode.rightnode == None:
    if currentNode.parent == None:
      B.root = None
    elif currentNode.parent.leftnode == currentNode:
      currentNode.parent.leftnode = None
    else:
      currentNode.parent.rightnode = None

  #Segundo caso: El nodo tiene solamente un hijo
  #Caso que el hijo este a la izquierda
  elif currentNode.leftnode != None and currentNode.rightnode == None:
    if currentNode.parent == None:
      B.root = currentNode.leftnode
      B.root.parent = None
    elif currentNode.parent.leftnode == currentNode:
      currentNode.leftnode.parent = currentNode.parent
      currentNode.parent.leftnode = currentNode.leftnode
    else:
      currentNode.leftnode.parent = currentNode.parent
      currentNode.parent.rightnode = currentNode.leftnode

  #Caso que el hijo este a la derecha
  elif currentNode.leftnode == None and currentNode.rightnode != None:
    if currentNode.parent == None:
      B.root = currentNode.rightnode
      B.root.parent = None
    elif currentNode.parent.leftnode == currentNode:
      currentNode.rightnode.parent = currentNode.parent
      currentNode.parent.leftnode = currentNode.rightnode
    else:
      currentNode.rightnode.parent = currentNode.parent
      currentNode.parent.rightnode = currentNode.rightnode

  #Caso que el nodo tenga dos hijos
  else:
    #Busca el mayor de los menores
    findNode = currentNode.leftnode
    while findNode.rightnode != None:
      findNode = findNode.rightnode
    currentNode.value = findNode.value
    return delete_nodeAVL(B, findNode)
  return currentNode.key


#Recorre una arbol en amplitud
#Devuelve una lista enlazada representando el recorrido
def traverseBreadFirst(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    insert(L, B.root, 0)
    addtraverseBreadFirst(L, L.head, 1)
    return L


def addtraverseBreadFirst(L, currentNode, position):
  if currentNode.value.leftnode != None:
    insert(L, currentNode.value.leftnode, position)
    position += 1
  if currentNode.value.rightnode != None:
    insert(L, currentNode.value.rightnode, position)
    position += 1
  if currentNode.nextNode != None:
    addtraverseBreadFirst(L, currentNode.nextNode, position)
  currentNode.value = currentNode.value.value


#Recorre un arbol binario en pre-orden
#Devuelve el recorrido en una lista enlazada
def traverseInPreOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    traverseInPreOrderR(L, B.root)
    reverse(L)
    return L


def traverseInPreOrderR(L, currentNode):
  add(L, currentNode.value)
  if currentNode.leftnode != None:
    traverseInPreOrderR(L, currentNode.leftnode)
  if currentNode.rightnode != None:
    traverseInPreOrderR(L, currentNode.rightnode)


#Recorre un arbol binario en in-orden
#Devuelve el recorrido en una lista enlazada
def traverseInOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    traverseInOrderR(L, B.root)
    reverse(L)
    return L


def traverseInOrderR(L, currentNode):
  if currentNode.leftnode != None:
    traverseInOrderR(L, currentNode.leftnode)
  add(L, currentNode.value)
  if currentNode.rightnode != None:
    traverseInOrderR(L, currentNode.rightnode)


#Recorre un arbol binario en post-orden
#Devuelve el recorrido en una lista enlazada
def traverseInPostOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    traverseInPostOrderR(L, B.root)
    reverse(L)
    return L


def traverseInPostOrderR(L, currentNode):
  if currentNode.leftnode != None:
    traverseInPostOrderR(L, currentNode.leftnode)
  if currentNode.rightnode != None:
    traverseInPostOrderR(L, currentNode.rightnode)
  add(L, currentNode.value)


#Elimina un nodo a través de la key
#Devuelve la key del nodo eliminado
def deleteKey(B, key):
  if B.root == None:
    return
  else:
    return deleteKeyR(B, B.root, key)


def deleteKeyR(B, currentNode, key):
  if currentNode.key == key:
    return delete_nodeAVL(B, currentNode)
  else:
    if currentNode.leftnode != None:
      Left = deleteKeyR(B, currentNode.leftnode, key)
      if Left != None:
        return Left
    if currentNode.rightnode != None:
      Right = deleteKeyR(B, currentNode.rightnode, key)
      if Right != None:
        return Right


#Accede a un elemento de un árbol AVL a través de una key
#Devuelve None si no puede encontrar dicho elemento
def accessAVL(B, key):
  if B.root == None:
    return
  else:
    return accessAVL(B, B.root, key)


def accessAVLR(B, currentNode, key):
  if currentNode.key == key:
    return currentNode.value
  else:
    if currentNode.leftnode != None:
      Left = accessAVLR(B, currentNode.leftnode, key)
      if Left != None:
        return Left
    if currentNode.rightnode != None:
      Right = accessAVLR(B, currentNode.rightnode, key)
      if Right != None:
        return Right


#Actualiza un elemento en la key seleccionada de un arbol AVL
#Devuelve la key si logra actualizarse, de lo contrario devuelve None
def updateAVL(B, element, key):
  if B.root == None:
    return None
  else:
    return updateAVLR(B.root, element, key)


def updateAVLR(currentNode, element, key):
  if currentNode.key == key:
    currentNode.value = element
    return key
  if currentNode.leftnode != None:
    Left = updateAVLR(currentNode.leftnode, element, key)
    if Left != None:
      return Left
  if currentNode.rightnode != None:
    Right = updateAVLR(currentNode.rightnode, element, key)
    if Right != None:
      return Right
