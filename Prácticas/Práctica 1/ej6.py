def vuelto(B, c):
    # Caso base: Si c es 0, hemos alcanzado el objetivo exactamente.
    if c == 0:
        return (0, 0)  # No exceso, 0 billetes usados.

    # Si ya no hay billetes para considerar y no hemos alcanzado el objetivo.
    if len(B) == 0 and c > 0:
        return None  # Imposible alcanzar c con los billetes dados.

    # Consideramos b el primer billete en B.
    b = B[0]
    
    # Solo hay un billete, entonces paga con ese
    if len(B) == 1 and b > c:
        return (b - c, 1)
    
    # Probamos dos opciones: no usar el billete actual y usar el billete actual.
    # No usar b
    opcion1= vuelto(B[1:],c)
    # Usar b y sumar 1 al resultado de esta opción
    opcion2 = vuelto(B[1:],c-b)
    if opcion2 is not None:
        opcion2 = (opcion2[0], 1 + opcion2[1])
    
    # elegir la opción que minimiza la cantidad de billetes usadsos.
    if opcion1 is None and opcion2 is not None:
        return opcion2
    elif opcion2 is None and opcion1 is not None:
        return opcion1
    elif opcion1 is not None and opcion2 is not None:
        ## Revisamos el min
        return min(opcion1, opcion2)
    else:
        return None

rta = vuelto([100,50,50,100], 120)
print(rta[0])
print(rta[1])

#Complejidad: O(2^n) xq ve todos los caminos agregando o no agregando cada billete 
