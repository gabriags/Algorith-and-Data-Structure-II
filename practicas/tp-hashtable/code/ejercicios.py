from dictionary import *

#Ejercicio 3
def ex3():
    i = 61
    while i<=65:
        A = ((1000**(1/2))-1)/2
        print(int(6*((i*A)%1)))
        i+=1

#Ejercicio 4
#Determina si un string es permutacion de otro
#Su tiempo de ejecucion es O(m**2) siendo m la longitud de cadena
#Seria más optimo si delete retornara True o False en lugar de D
#De esta forma podriamos detener la ejecucion si no logra eleminar un caracter de string2 en D
def isPermutation(string1,string2):
    n = len(string1)
    m = len(string2)

    #Check de ancho de palabra
    if m == n:
        D = Dictionary(m)
        #inserto string 1 en D
        for i in range(0,len(string1)):
            insert(D,string1[i],string1[i])

        #Elimino string 2 en D
        for i in range(0,len(string2)):
            delete(D,string2[i])
        
        flag = True
        for i in range(0,len(D)):
            if D[i]!=None:
                flag = False
        if flag:
            return flag
    return False


#Ejercicio 5
#Determina si una lista L posee elementos unicos
#Busca el elemento en D, si existe previamente devuelve False
def Unique(D,L):
    if L == None:
        return
    else:
        for i in range(0,len(L)):
            flag = search(D,L[i])
            if flag == None:
                insert(D,L[i],L[i])
            else:
                return False
        return True

#Ejercicio 6
#El formato de las direcciones es cddddccc
#Hay 26 letras desde la A-Z para c y 10 digitos desde 0-9 para d
#Genero una clave unica
def postalHash(k,m):
    cityreference = 0
    streetreference = ''
    count1 = 3
    for i in range(0,8):
        if (i<=0 or i>=5):
            print(ord(k[i])-ord('A'))
            print(10**count1)
            cityreference = cityreference + (ord(k[i])-ord('A'))*(100**count1)
            count1 -= 1
        else:
            streetreference += k[i]
    
    keystr = str(cityreference) + streetreference
    key = int(keystr)                    
    #Utilizo metodo de la multiplicaion con A = ((5**(1/2))-1)/2
    A = ((5**(1/2))-1)/2
    return int(m*((key*A)%1))

#Ejercicio 7
'''
idea
    Preparacion
        Crear una variable newString que formara la nueva cadena
        Contar de 2 en 2 cada vez que inserta caracteres en newString
        Recorrer la cadena siguiendo los pasos
    Pasos
        1. Buscar el primer caracter en el hash
            a.Si existe, actualizamos su value contando las repeticiones
            b.Si no existe, introducirlo en el hash
        2.Actualizar el siguiente caracter a buscar
            LLevar un flag con el ultimo caracter buscado
            a. Si el nuevo caracter es distinto, insertar el anterior caracter con su value en el newString y borrarlo del hash
            b. Lo mismo si se trata del ultimo caracter del recorrido
        Comparar el tamaño de ambos string y devolver el menor
'''
#Comprime una palabra
#Recibe un diccionario y una palabra
#Devuelve la palabra o la compresion segun cual sea más corta
#Coste O(n)
def compresion(D,word):
    n = len(word)
    newString = ''
    newStringlen = 0
    lastInsert = word[0]
    for i in range(0,n):
        exist = search(D,word[i])
        if exist == None:
            insert(D,word[i],1)
        else:
            update(D,word[i],exist+1)
        if lastInsert != word[i] or i == n-1:
            newString += lastInsert+str(search(D,lastInsert))
            newStringlen += 2
            delete(D,lastInsert)
            lastInsert = word[i]
    if n>=newStringlen:
        return newString
    else:
        return word
        

#Ejercicio 8
'''
Idea
    Tomar el string S y insertar en D subcadenas de S del tamaño de P
    Luego buscar si P existe en D
    La cantidad de inserciones sera len(S)-len(P)
    La complejidad es O(1) en el search
    
'''
#Determina si una cadena S se encuentra como subcadena dentro de P
#Devuelte True al encontrar la primera instancia de S en P
#Devuelve False si no existe en P
def isInside(D,S,P):
    m = len(S)
    n = len(P)
    if m>=n:
        for i in range(0,m-n+1):
            insert(D,S[i:i+n],i)
        exist = search(D,P)
        if exist!=None:
            return True
        else:
            return False
        
#Ejercicio 9
#Determina si un S de enteros en subconjuto de T
#Devuelve True o False segun sea
def subSet(D,S,T):
    m = len(S)
    n = len(T)
    if n>=m:
        for i in range(0,n):
            exist = search(D,T[i])
            if exist!=None:
                update(D,T[i],exist+1)
            else:
                insert(D,T[i],1)

        for i in range(0,m):
            exist = search(D,S[i])
            if exist!=None:
                if exist == 0:
                    return False
                else:
                    update(D,S[i],exist-1)
            else:
                return False
        return True
