
#Simple case of pattern maching
#O((n-m+1)*m)
def naive_pattern_matching(t,p):
  m = len(p)
  n = len(t)
  if n>=m:
    for s in range(0,n-m):
      if  t[0+s:m+s] == p:
        print(p, "found at", s)
        return True
  return False


#Rabin Karp
#Complex: O((n-m+1)*m) prom 0(m+n)
def patternRK(t,p):
  m = len(p)
  n = len(t)
  if type(t) == str:

    patternHash = firsthashRK(p,m)
    print(f'patt: {patternHash}')
    subHash = firsthashRK(t[0:m],m)
    if subHash == patternHash:
      print(f'{p} found at 0')
    else:
      for i in range(0,n-m):
        subHash = secondhashRK(subHash,t[i],t[m+i],m)
        if subHash == patternHash:
          print(f'pattern found at {i+1}')


#This a weighted hash
#All positions of word has a weight
def firsthashRK(word,m):
  hash = 0
  for i in range(0,m):
    hash += ord(word[i])*(128**(m-1-i))
  return hash

def secondhashRK(befhash,firstchar,nextchar,m):
  hash = 128*(befhash - ((128**(m-1))* ord(firstchar))) + ord(nextchar)
  return hash
