def mergeSort(A):
    if len(A) <= 1:
        return A
    
    A1 = mergeSort(A[:len(A)//2])
    A2 = mergeSort(A[len(A)//2 : len(A)])
    
    return merge(A1,A2)

def merge(A1,A2):
    res = []
    i = 0
    j = 0
    
    while (i != len(A1)) and (j != len(A2)):
        if A1[i] <= A2[j]:
            res.append(A1[i])
            i+=1
        else:
            res.append(A2[j])
            j+=1
            
    # Agregar los elementos restantes de A1 o A2 a la lista res
    if j >= len(A2):
        while i < len(A1):
            res.append(A1[i])
            i += 1
    else:
        while j < len(A2):
            res.append(A2[j])
            j += 1


    return res 

A=[7,2,7,8,9,11,2,5,4]

print(mergeSort(A))


'''
Complejidad:
T(n) = aT(n/c) + bn^d = 2T(n/2) + n
a = 2
c = 2
d = 1
log_c_a = log_2_2 = 1 

Por teorema maestro:

f(n) in theeta(n^log_c_a) (mi f(n) = n)
n in theeta(n^1) ==> n in theeta(n) 

Entonces entramos en el segundo caso de teorema maestro(ver que a=c y f(n) cumple)
==> T(n) in O(n log n)
'''