memo = {}
A = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

def travesia(i, j):
    if i >= len(A) or j >= len(A[0]):
        return float('inf')
    
    if i == len(A) - 1 and j == len(A[0]) - 1:
        return max(1, 1 - A[i][j])
    
    if (i, j) not in memo:
        abajo = travesia(i, j + 1)
        derecha = travesia(i + 1, j)
        memo[(i, j)] = max(1, min(abajo, derecha) - A[i][j])
    
    return memo[(i, j)]

# Calcular el resultado de travesia para cada posición (i, j)
for i in range(len(A)):
    for j in range(len(A[0])):
        travesia(i, j)

# Imprimir la matriz memo
print("Matriz memo:")
for i in range(max(len(A), len(A[0]))):
    for j in range(max(len(A), len(A[0]))):
        if (i, j) in memo:
            print(f"{memo[(i, j)]:>5}", end=" ")
        else:
            print(f"   - ", end=" ")
    print()

# Imprimir la matriz A
print("\nMatriz A:")
for row in A:
    print("      ".join(map(str, row)))

#Complejidad Temporal: O(nm) xq recorre toda la matriz pero en cada nodo solo realiza operaciones en O(1)
#Complejidad Espacial: O(nm)

def travesiaBottomUp(A): #funca patriki
    memoi = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(1)
        memoi.append(fila)
    
    #una vez inicializada en 1, llenamos la matriz de atras para adelante abajo para arriba
    #aparte llenamos el "caso base"
    memoi[len(A)-1][len(A[0])-1] = max(1, 1 - A[len(A)-1][len(A[0])-1])
    
    for i in range (len(A)-2, -1, -1):
        for j in range(len(A[0])-2, -1, -1):
            memoi[i][j] = max(1, min(memoi[i][j+1], memoi[i+1][j]) - A[i][j])
            
    return memoi

print(travesiaBottomUp(A))
