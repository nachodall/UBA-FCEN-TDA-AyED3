def es_mas_a_la_izquierda(A):
    n = len(A)
    
    # Caso base: si el arreglo tiene un solo elemento, es "más a la izquierda"
    if n == 1:
        return True
    
    # Calculamos la suma de la mitad izquierda y la mitad derecha del arreglo
    mitad = n // 2
    suma_izquierda = sum(A[:mitad])
    suma_derecha = sum(A[mitad:])
    
    # Verificamos si la suma de la mitad izquierda es mayor que la de la mitad derecha
    if suma_izquierda > suma_derecha:
        # Si es así, verificamos recursivamente si cada mitad es "más a la izquierda"
        return es_mas_a_la_izquierda(A[:mitad]) and es_mas_a_la_izquierda(A[mitad:])
    else:
        return False

A = [8, 6, 7, 4, 5, 1, 3, 2]
B = [8, 4, 7, 6, 5, 1, 3, 2]

print(es_mas_a_la_izquierda(A))  # Devuelve True
print(es_mas_a_la_izquierda(B))  # Devuelve False
