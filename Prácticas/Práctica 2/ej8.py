def encontrarFalse(m):
    for i in range(len(m)):
        j = 0
        while j < len(m[i]):
            if not m[i][j]:
                if conjuncionSubmatriz(m, i, i, 0, j):
                    return (i, j)
            j += 1
    return (-1, -1)
 
def conjuncionSubmatriz(m, i0, i1, j0, j1):
    conjuncion = True
    for i in range(i0, i1 + 1):
        for j in range(j0, j1 + 1):
            conjuncion = conjuncion and m[i][j]
    return conjuncion

matriz = [
    [True, True, True, True],
    [True, True, True, True],
    [True, True, False, True],
    [True, True, True, True]
]

res = encontrarFalse(matriz)
print(res)
