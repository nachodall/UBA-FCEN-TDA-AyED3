
def mgnTopDown(j, c):
    if (j, c) in memo:  # Verificar si el resultado ya se calculó.
        return memo[(j, c)]
    
    if c < 0 or c > j:  # Caso base para condiciones invalidas.
        return float('-inf')
    if c == 0 and j == 0:
        return 0  # Caso base, día 0 con cero asteroides.
    if j == 0 and c != 0:
        return float('-inf')
    
    # La ganancia se calcula considerando la compra, venta o no operar.
    comprar = mgnTopDown(j-1, c-1) - p[j-1] if c > 0 else float('-inf')
    vender = mgnTopDown(j-1, c+1) + p[j-1] if c < j else float('-inf')
    no_operar = mgnTopDown(j-1, c)
    
    memo[(j, c)] = max(comprar, vender, no_operar)  # Se almacena el resultado en la memoria.
    return memo[(j, c)]

memo = {}
p = [2,3,5,6]
print(mgnTopDown(len(p), 0))

#complejidad: O(jc) 