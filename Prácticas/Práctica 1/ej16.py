def renault12(C, estaciones):
    paradas = []
    nafta = C
    
    for i in range(len(estaciones)-1):
        distancia_hasta_siguiente = estaciones[i+1] - estaciones[i]
        
        if nafta < distancia_hasta_siguiente:
            paradas.append(estaciones[i])
            nafta = C - distancia_hasta_siguiente  # la nafta que va a tener en la estacion que viene
        else:
            nafta -= distancia_hasta_siguiente  # no parar
            
    return paradas, len(paradas)


C = 150
estaciones = [0,100,200,250,300,400]
paradas, cant = renault12(C,estaciones)
print("La cant de estaciones a parar es: ",cant," y son: ")
for parada in paradas:
    print(parada)