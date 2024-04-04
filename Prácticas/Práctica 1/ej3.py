# las lineas que no tienen complejidad es O(1)
# la complejidad de la memoria es O(n^2 + k) por que se crea la matriz y dos array de longitud k que son los de parcial y res, ademas del array de candidatos que es O(n) que se va con n cuadrado 
# la complejidad temporal es O(k! * k^2), el n! cuadrado es de calcular las combinaciones tal que;
#                                           n en el nivel 0
#                                           n (n-1) en el nivel 1
#                                           n (n-1)...(n-k) en el nivel k
#                                           el k^2 viene de calcular la sumatoria para cada posible solucion
from typing import List

class Solucion:
    def __init__(self, valor_entero: int, conjunto: List[int]):
        self.valor: int = valor_entero
        self.indices: List[int] = conjunto

def maxiSubconjunto(m: List[List[int]], i: int, k: int, candidatos: List[bool], parcial: Solucion, res: Solucion):
    if i == k: #caso base
        parcial.valor = sumarValoresParciales(m, parcial); #O(k^2)
        if parcial.valor > res.valor:
            res = parcial.copy();
    
    #magia
    for j in range(0,len(candidatos)): #O(j) con j el tamaño de la mastriz
        if candidatos[j]: # si el j ya esta en el conjunto paso a la prox iteracion xq es un conjunto no puede estar 2 veces el mismo numero
            continue; # skip a la proxima iteracion

        # ahora vamos a ver si el numero es mas chico q el anterior, esto es para no ver todas las permutaciones
        # vemos q solo necesito las permutaciones "ordenadas", o sea si vimos el {1,2,4} no volvemos a ver el {1,4,2}
        if i > 0 & parcial.indices[i-1] > j: #el i > 0 es obvio xq no hay anterior
            return; # pincho esta solucion 
        
        #como no esta en el conjunto lo agregamos 
        parcial.indices.append(j);
        candidatos[j] = True;
        i+=1; #el i es para controlar cuando llegamos al k 

        #llamada recursiva
        maxiSubconjunto(m,i,k,candidatos,parcial,res); #O(llamada recursiva)

        #backtracking
        candidatos[j] = False;
        i-=1; 


    return; 

def sumarValoresParciales(m, parcial):
    acc = 0;
    for indice in parcial.indices:
        for indice2 in parcial.indices:
            if indice != indice2:
                acc += m[indice][indice2];
    return acc;