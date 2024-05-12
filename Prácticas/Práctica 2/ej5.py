import numpy as np

A = np.array([[1, 2],
              [3, 4]])

def potenciaMatriz(M,n):
    return np.linalg.matrix_power(M,n)

def sumaDePotencias(M,n):
    if n == 1:
        return M
    
    if n % 2 == 0:
        aux = potenciaMatriz(M, n//2)
        return np.dot(aux, aux)
    
    else:
        aux = potenciaMatriz(M, (n-1)//2)
        aux2 = np.dot(aux, aux)
        return np.dot(aux2, M)

#es analogo al ejercicio de potencias logaritmicas pues aca si el exponente es par, dividimos en 2 sucesivamente y luego las vamos juntando