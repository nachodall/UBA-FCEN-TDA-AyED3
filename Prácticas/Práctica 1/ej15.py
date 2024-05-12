# la estrategia golosa es ir sumando del menor al mayor para eso hay q ordenar 

def sumaGolosa(X):
    X = sorted(X)
    acc = 0
    for num in X:
        acc = acc + num 
    return acc 
