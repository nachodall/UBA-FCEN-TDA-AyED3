#consultar
memo = {}
W = [19, 7, 5, 6, 1]
S = [15, 13, 7, 8, 2]
n = len(W)

def pila(i,j,w_acum):
    if i > n-1:
        return 0
    
    if j != float('-inf'):
        if W[i] + w_acum > S[j] or S[i] < w_acum:
            return pila(i+1,j,w_acum)
    
    if (i,j,w_acum) not in memo:
        noAgregarlo = pila(i+1, j, w_acum)
        agregarlo = 1 + pila(i+1, i, w_acum + W[i])
        memo[(i,j,w_acum)] = max(noAgregarlo, agregarlo)
        
    return memo[(i,j,w_acum)]

print(pila(0,float('-inf'),0))