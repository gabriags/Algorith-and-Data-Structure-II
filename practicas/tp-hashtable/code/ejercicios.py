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


