"""
Es una modificacion de mergeSort  ==> su complejidad O(n log n)
"""

def mergeSortCounter(A):
    if len(A) <= 1:
        return A,0
    
    A1, inversiones1 = mergeSortCounter(A[:len(A)//2])
    A2, inversiones2 = mergeSortCounter(A[len(A)//2 : len(A)])
    
    merged, inversionesMerged = count(A1,A2)
    
    return merged, inversiones1 + inversiones2 + inversionesMerged

def count(A1,A2):
    res = []
    cont = 0
    i = 0
    j = 0
    
    while (i != len(A1)) and (j != len(A2)):
        if A1[i] <= A2[j]:
            res.append(A1[i])
            i+=1
        else:
            res.append(A2[j])
            cont+=1
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


    return res,cont

A = [1,2,5,4,6,3] 
sorted_A, inversiones = mergeSortCounter(A)
print("Arreglo ordenado:", sorted_A)
print("Número de inversiones:", inversiones)