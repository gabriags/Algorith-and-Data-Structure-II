#Automato Finite
#Pattern Matching

#IN: Text and Pattern
#OUT: Prints where the pattern is in T
def patternAEF(T,P):
    Alf = createAlf(T)
    delta = createAutomate(P,Alf)
    AEF(T,delta,len(P),Alf) #Matching

#This the automato working
#delta is the transicion table, it columns depends of the index in charlist
#charlist is the alfabet sorted, each position is a colum at delta   
def AEF(T,delta,m,charList):
    n = len(T)
    q = 0
    
    for i in range(0,n):
      q = delta[q][charList.index(T[i])]
      if q == m:
          print(f'pattern ocurrs with shift {i-m+1}')

#Creates a list of alfabet T
#IN: Text
#Out: Alfabet sorted of T
def createAlf(T):
  #Obteins the alfabet of T
  Alf = sorted(list(set(T)))
  return Alf

#Create a table for transicion function of automaton
#IN: Pattern and list of alfabet
#Complex O(m*|Alf|)
def createAutomate(P,Alf):
  baseStr = nextStr =  ''
  subP = ''
  m = len(P)
  n = len(Alf)
  Table  = createMatrix(m+1,n,0)

  #Build the transicion function of automaton
  for i in range(0,m):
    subP += P[i]
    for j in range(0,n):
      nextStr += Alf[j]
      #print(f'subP: {subP}, nextStr: {nextStr}')
      Table[i][j] = findSufPre(subP,nextStr)
      nextStr = baseStr
    baseStr = nextStr =  subP 

  #For next character after matching
  for j in range(0,n):
    nextStr += Alf[j]
    #print(f'subP: {subP}, nextStr: {nextStr}')
    Table[m][j] = findSufPre(subP,nextStr)
    nextStr = baseStr
  
  return Table


#Count the largest prefix of P that is suffix of Pqa
def findSufPre(P,Pqa):
  m = len(Pqa) 
  n = len(P)   
  mayor = 0
  j = 1
  for i in range(m,m-n,-1):
    if P[0:j] == Pqa[m-j:m]:
      mayor = j
    j+=1
  return mayor


#Creates a matrix of size nxm of type mtype(integer,string)
def createMatrix(n,m,mtype):
	if type(mtype) == int:
		matrix = []
		for i in range(n):
			rows = [0]*m
			matrix.append(rows)
		return matrix
	
	elif type(mtype) == str:
		matrix = []
		for i in range(n):
			rows = ['']*m
			matrix.append(rows)
		return matrix

