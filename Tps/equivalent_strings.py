#consigna: https://vjudge.net/problem/CodeForces-559B

def equivalent_strings(a,b):
    if a == b:
        return True    
    
    if len(a) % 2 == 1: # Esto implica que los strings a dividir van a ser de longitud distinta
        return False
    
    middle = len(a)//2

    a1 = a[:middle]
    a2 = a[middle:]
    b1 = b[:middle]
    b2 = b[middle:]
    
    return (equivalent_strings(a1,b2) and equivalent_strings(a2,b1)) or  (equivalent_strings(a1,b1) and equivalent_strings(a2,b2))

a = str(input())
b = str(input())

if equivalent_strings(a,b):
    print("YES")
else:
    print("NO")