#Determina si en un array existen dos numeros que sumados den n
#O(n**2)
def Contiene_Suma(A,n):
    Asize = len(A)
    for i in range(0,Asize):
        sum = A[i]
        for j in range(i,Asize):
            if sum+A[j]==n:
                return True