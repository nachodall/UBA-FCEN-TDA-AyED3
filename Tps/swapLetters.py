#Consigna: https://vjudge.net/problem/CodeForces-1215C

def esPosible(n,s,t):
    cantidades = {'ab': 0,
                  'ba': 0}
    
    for i in range(n):
        if s[i] != t[i]:
            if s[i] == 'a':
                cantidades['ab'] += 1
            else:
                cantidades['ba'] += 1
                
    if (cantidades['ab'] + cantidades['ba']) % 2 == 1:
        return False
    else:
        return True

def diferenciarAB(n,s,t):
    AB = []
    BA = []
    
    for i in range(n):
        if s[i] != t[i]:
            if s[i] == 'a':
                AB.append(i+1)
            else:
                BA.append(i+1)
    
    return AB, BA    

n = int(input())
s = input()
t = input()

if not esPosible(n,s,t):
    print(-1)
    
else:
    #me guardo los indices donde aparecen AB, BA 
    AB, BA = diferenciarAB(n,s,t)
    movimientos = []
    
    i = 0
    j = 0
    
    #si son de longitud par, hago los cambios todo tranqui 
    
    while i < len(AB)-1:
        movimientos.append((AB[i], AB[i+1]))
        i = i+2
    
    while j < len(BA)-1:
        movimientos.append((BA[j], BA[j+1]))
        j = j+2
        
    #cuando tienen longitud impar hay que hacer un jeite extra
    if i < len(AB) and j < len(BA):
        movimientos.append((AB[i], AB[i]))
        movimientos.append((AB[i], BA[j]))
    
    print(len(movimientos))
    
    for (a,b) in movimientos:
        print(a, b)