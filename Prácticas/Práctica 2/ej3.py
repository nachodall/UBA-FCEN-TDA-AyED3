def potenciaLogaritmica(a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * potenciaLogaritmica(a, b - 1)
    else:
        return potenciaLogaritmica(a * a, b // 2)

a = 2
b = 10
print(potenciaLogaritmica(a, b)) 

'''
Complejidad:
T(n) = T(n/2) + O(1)
a = 1 pues tengo un solo subproblema
c = 2, pues divido en 2 el b 
f(n) = cte entonces primer caso de teorema maestro y complejidad O(log b)
'''


        
