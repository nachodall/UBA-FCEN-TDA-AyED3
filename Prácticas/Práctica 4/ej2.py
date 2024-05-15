def dfs(lista_de_adyacencias, vertice, visitados, padres, niveles, min_nivel_cubierto):
    visitados[vertice] = True
    for vecino in lista_de_adyacencias[vertice]:
        if not visitados[vecino]:
            niveles[vecino] = niveles[vertice] + 1
            padres[vecino] = vertice
            dfs(lista_de_adyacencias, vecino, visitados, padres, niveles, min_nivel_cubierto)
            min_nivel_cubierto[vertice] = min(min_nivel_cubierto[vertice], min_nivel_cubierto[vecino])
        elif vecino != padres[vertice]: # es un back edge
            min_nivel_cubierto[vertice] = min(min_nivel_cubierto[vertice], niveles[vecino])

def no_cubiertos(n, padres, niveles, min_nivel_cubierto):
    return [vertice for vertice in range(n) if min_nivel_cubierto[vertice] >= niveles[vertice] and padres[vertice] != -1]

def puentes(lista_de_adyacencias):
    n = len(lista_de_adyacencias)
    visitados = [False] * n
    padres = [-1] * n
    niveles = [0] * n
    min_nivel_cubierto = list(range(n))
    for vertice in range(n):
        if not visitados[vertice]:
            niveles[vertice] = 0
            dfs(lista_de_adyacencias, vertice, visitados, padres, niveles, min_nivel_cubierto)

    return [(padres[vertice], vertice) for vertice in no_cubiertos(n, padres, niveles, min_nivel_cubierto)]

# Ejemplo de uso:
grafo_ejemplo = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}

print("Puentes en el grafo:", puentes(grafo_ejemplo))
