#Knuth-Morris-Pratt
#Pattern Matching

#Find a pattern P in a text T with KMP method
#Complex: O(m)
def patternKMP(T,P):
    n = len(T)
    m = len(P)
    pi = createPi(P)
    q = 0

    for i in range(0,n):
        while (q>0 and P[q]!=T[i]):
           q = pi[q-1]
        if P[q] == T[i]:
          q += 1
        if q == m:
           print(f"Pattern occurs with shift {i-m+1}")
           q = pi[q-1]

#Create the array for kmp(pi)
#Complex O(m)
def createPi(P):
    pi = []
    Pq = Pk = ''
    for i in P:
        Pq += i
        q = findSufPre(Pk,Pq)
        pi.append(q)
        Pk = Pq

    return pi


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