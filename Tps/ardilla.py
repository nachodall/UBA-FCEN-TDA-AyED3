def ardilla(arboles,heights,f,bellotas):
    m = [[0]*arboles for _ in range(heights)] #memo de heights x arboles

    #arranco de h-max entonces me lleno en la memo la primera fila representando la hMax
    for i in range(arboles):
        m[0][i] = bellotas[i][0]
        
    #lleno la memo en bottom-up
    for h in range(1,heights):
        if h-f >= 0:
            maxh = max(m[h-f]) # el maximo de cualquier arbol en la altura bajando 
        else:
            maxh = 0 #no se puede bajar mas
        for t in range(arboles):
            m[h][t] = max(m[h-1][t], maxh) + bellotas[h][t] #el maximo entre quedarme en este arbol, o pasar a cualquier otro arbol 
        
    return max(m[heights-1]) # de que tope de que arbol arranco

c = int(input())
for _ in range(c):
    t,h,f = map(int, input().split())
    bellotas_map = [[0] * h for _ in range(t)]
    for tree in range(t):
        bellotas_tree = list(map(int, input().split()))
        for a in bellotas_tree[1:]:
            bellotas_map[tree][a-1] += 1
    print(ardilla(t,h,f,bellotas_map))
        
    