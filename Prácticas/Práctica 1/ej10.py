#consultar complejidad
memo = {}  
W = [19, 7, 5, 6, 1]  
S = [15, 13, 7, 8, 2]  
n = len(W)  

def pila(i, k):
    if i == -1:
        return 0  # Caso base: Si hemos procesado todas las cajas (i == -1), no podemos apilar más cajas
    
    if k > S[i]:
        return pila(i - 1, k)  # Si el peso acumulado supera el soporte de la caja actual, pasamos a la siguiente caja
    
    if (i, k) not in memo:  # Si el resultado no está memoizado, lo calculamos y lo almacenamos
        # Calculamos la cantidad máxima de cajas que se pueden apilar si NO agregamos la caja actual
        no_agregar = pila(i - 1, k)
        # Calculamos la cantidad máxima de cajas que se pueden apilar SI agregamos la caja actual
        agregar = pila(i - 1, k + W[i]) + 1
        # Tomamos el máximo entre ambas opciones y lo almacenamos en el diccionario de memoización
        memo[(i, k)] = max(no_agregar, agregar)
    
    # Devolvemos la cantidad máxima de cajas que se pueden apilar considerando la caja actual y el peso acumulado
    return memo[(i, k)]

# Llamamos a la función top_down con el índice de la última caja (n-1) y un peso acumulado inicial de 0
print(pila(n - 1, 0))

#complejidad: O(n * sum(W[i]) ya que en cada llamada recursiva llamamos con un distinto i y un peso distinto que como maximo es todos los pesos acumulados
combinatorio