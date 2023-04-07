from linkedlist import LinkedList, add, length
from linkedlist import delete as deleteLL


class Trie:
  root = None


class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = None


#Inserta un elemento en un Trie
#Ingresa un Trie y un elemento
def insert(T, element):
  if T.root == None:
    Node = TrieNode()
    Node.children = LinkedList()
    T.root = Node
  insertR(T, element, 0, T.root)


def insertR(T, element, charposition, currentNode):

  #Recorro los hijos
  currentChild = currentNode.children.head
  flag = False
  while currentChild != None and flag == False:
    #Primer Caso: Encuentra una coincidencia de caracteres
    if currentChild.value.key == element[charposition]:
      Node = currentChild.value
      flag = True
    currentChild = currentChild.nextNode

  if flag == False:
    #Segundo Caso: No hay antecedentes
    Node = TrieNode()
    Node.key = element[charposition]
    Node.children = LinkedList()
    Node.parent = currentNode
    add(currentNode.children, Node)

  #Determino si el caracter agregado es el final de la palabra
  if charposition == len(element) - 1:
    Node.isEndOfWord = True
  else:
    #Continuo con el siguiente caracter
    insertR(T, element, charposition + 1, Node)


#Busca un elemento en un Trie
#Devuelve True si existe el elemento, devuelve None si no existe
def search(T, element):
  if T.root == None:
    return False
  else:
    return searchR(T.root.children.head, 0, element)


def searchR(currentNode, charPosition, element):
  flag = False
  while currentNode != None and flag == False:

    #veo coincidencia
    if currentNode.value.key == element[charPosition]:
      flag = True
      #Caso que exista la palabra
      if currentNode.value.isEndOfWord == True and charPosition == (
          len(element) - 1):
        return True
      elif currentNode.value.isEndOfWord == None and charPosition == (
          len(element) - 1):
        return False
      elif charPosition < (len(element) - 1):
        charPosition += 1
        return searchR(currentNode.value.children.head, charPosition, element)

    currentNode = currentNode.nextNode
  return False


#Elimino elemento de una Trie
#Ingresa un Trie y un elemento
#Devuelve True si logra eliminar el elemento y False si no lo logra
def delete(T, element):
  if T.root == None:
    return False
  else:
    lastNode = findEndEle(T, element)
    if lastNode != None:
      return deleteword(T, element, lastNode)
    else:
      return False


#Busca el nodo correspondiente al ultimo caracter de un elemento en un Trie
#Ingresa un Trie y un elemento
#Devuelve el nodo
def findEndEle(T, element):
  if T.root == None:
    return None
  else:
    return findEndEleR(T.root.children.head, 0, element)


def findEndEleR(currentNode, charPosition, element):
  flag = False
  while currentNode != None and flag == False:
    if currentNode.value.key == element[charPosition]:
      flag = True
      if currentNode.value.isEndOfWord == True and charPosition == (
          len(element) - 1):
        return currentNode.value
      elif currentNode.value.isEndOfWord == None and charPosition == (
          len(element) - 1):
        return None
      elif charPosition < (len(element) - 1):
        charPosition += 1
        return findEndEleR(currentNode.value.children.head, charPosition,
                           element)
    currentNode = currentNode.nextNode
  return None


#Elimina un elemento de un Trie
#Ingresa un Trie, un elemento y el nodo correspondiente al ultimo caracter del elemento
def deleteword(T, element, currentNode):
  if length(currentNode.children) != 0:
    currentNode.isEndOfWord = None
  else:
    flag = False
    while currentNode.value != None and flag == False:
      parent = currentNode.parent
      if length(parent.children) > 1:
        flag = True
      deleteLL(parent.children, currentNode)
      currentNode = parent
  return True


#Busca elementos en un trie con patron p y longitud n
#Ingresa un Trie, un patron y la longitud
#Devuelve None si no es posible buscar, delocontrario devuelve una linked list
def findPattern(T, p, n):
  if T.root == None:
    return None
  if len(p) > n:
    return None
  else:

    L = LinkedList()
    lastNode = findEndEle(T, p)
    if lastNode != None:
      if p == n:
        add(L, p)
      else:
        currentNode = lastNode.children.head
        while currentNode != None:
          findPatternR(currentNode, p, n, L)
          currentNode = currentNode.nextNode
    return L


def findPatternR(currentNode, word, maxLen, L):
  if currentNode != None:
    if len(word) < maxLen:
      word = word + currentNode.value.key
    if len(word) == maxLen and currentNode.value.isEndOfWord == True:
      add(L, word)
    elif len(word) == maxLen and currentNode.value.isEndOfWord == None:
      return
    else:
      currentNode = currentNode.value.children.head
      while currentNode != None:
        findPatternR(currentNode, word, maxLen, L)
        currentNode = currentNode.nextNode
  return


#Determina si todos los elementos de un Trie T1 estan dentro de otro Trie T2
def subTrie(T1, T2, string):
  flag = True
  currentNode = T1.children.head
  while currentNode != None:
    word = string + currentNode.value.key
    if currentNode.value.isEndOfWord:
      flag = search(T2, word)
    if flag == False:
      return False
    else:
      printTrie(currentNode.value, word)
    currentNode = currentNode.nextNode


#Imprime un Trie
#Utiliza length de linked list
'''
El formato es:
Elemento
Prefijo_A/
  Elemento_A1
  Elemento_A2
  ...

ElementoB -> ElementoC
donde elemento B es un elemento dentro del elemento C
'''


def printTrie(trieNode, string):
  currentNode = trieNode.children.head
  while currentNode != None:
    word = string + currentNode.value.key
    if length(currentNode.value.children) > 1:
      print(word + '/')
    #Imprime una palabra dentro de otra
    elif currentNode.value.isEndOfWord and currentNode.value.children.head != None:
      print(word + '->', end='')
    elif currentNode.value.isEndOfWord:
      print(word)
    printTrie(currentNode.value, word)
    currentNode = currentNode.nextNode
