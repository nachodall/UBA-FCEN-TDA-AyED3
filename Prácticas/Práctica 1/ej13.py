def parejasDeBaile(personas1, personas2):
    i = 0
    j = 0
    res = 0
    
    while i < len(personas1) and j < len(personas2):
        if abs(personas1[i] - personas2[j]) <= 1:
            res+=1
            i+=1
            j+=1
        elif personas1[i] > personas2[j]: #como estan ordenados me quedo con el mayor
            j+=1
        else:
            i+=1
    return res

personas1 = [1,2,4,6]
personas2 = [1,2,3]
print(parejasDeBaile(personas1,personas2))

#Complejidad O(min(n,m)), Espacial Auxiliar: O(1)