def mcTopDown(i,j):
    if j == i+1:
        return 0
    
    if (i,j) not in memo:
        minimoCoste = float('inf')
        
        for k in range(i+1,j):
            minimoK = mcTopDown(i,k) + mcTopDown(k,j) + (C[j] - C[i])
            if minimoK < minimoCoste:
                minimoCoste = minimoK
                
        memo[(i,j)] = minimoCoste
        
    return memo[(i,j)]   

longitud = 10
memo = {}
C = [2,4,7]
C = [0] + C + [longitud] #necesto agregar el comienzo y el final de mi vara
print(mcTopDown(0,len(C)-1))

#complejidad espacial: O(n^2)
#complejidad temporal: O(n^3) xq recorres toda la matriz y para casillero te cuesta O(n) calcular el min(i<k<j)
