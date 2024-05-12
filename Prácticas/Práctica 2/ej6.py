#diametro??
class Ab:
    def __init__(self, dato, izq, der):
        self.dato = dato
        self.izq = izq
        self.der = der

def distanciaMaxima(nodo):
    if nodo == None:
        return 1
    
    distanciaIzq = altura(nodo.izq)
    distanciaDer = altura(nodo.der)
    
    return distanciaDer + distanciaIzq + 1

def altura(nodo):
    if nodo is None:
        return 0
    
    else:
        left_height = altura(nodo.izq)
        right_height = altura(nodo.der)
        
        return max(left_height, right_height) + 1