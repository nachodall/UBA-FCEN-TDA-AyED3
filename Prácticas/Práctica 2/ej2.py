def indiceEspejo(A):
    if len(A) == 0:
        return False
    
    mid = len(A) // 2
    
    if A[mid] == mid:
        return True
    
    if A[mid] > mid:
        return indiceEspejo(A[:mid])  # Buscar en la mitad izquierda, incluyendo el elemento 'mid'
    else:
        return indiceEspejo(A[mid+1:])  # Buscar en la mitad derecha, excluyendo el elemento 'mid'

# Ejemplo de uso
arr = [-4, -1, 2, 4, 7]
print(indiceEspejo(arr))  # Devuelve True

'''
Complejidad: Como parto el array en 2 partes y me quedo solo con una:
a = 1, c = 2, d = 0/1?
entonces:
T(n) = 1T(n/2) + O(1)
Comparando f(n) con n^log_c_a = n^0 = 1 entones entramos en el segundo caso del teorema maestro
y la complejidad es O(n^0 log n) = O(log n)   
'''