from typing import List;

class Jugador:
    def __init__(self, nombre, ataque, defensa):
        self.nombre = nombre;
        self.ataque = ataque;
        self.defensa = defensa;


def buscarFormacionIdeal(jugadores):
    def armarDefensores(usados):
        rta: List[Jugador] = []
        for jugador in jugadores:
            if jugador not in usados:
                rta.append(jugador)
        return rta

    def backtracking(delanterosParcial, defensoresParcial, i, usados, delanteros, defensores):
        nonlocal max_ataque, max_defensa #la clave de todo 
        
        #caso base 
        if i == 5:
            defensoresParcial = armarDefensores(usados)
            sumaParcialAtaque = sum(jugador.ataque for jugador in delanterosParcial)
            sumaParcialDefensa = sum(jugador.defensa for jugador in defensoresParcial)

            if (sumaParcialAtaque > max_ataque) or ((sumaParcialAtaque == max_ataque) and (sumaParcialDefensa > max_defensa)):
                max_ataque = sumaParcialAtaque
                max_defensa = sumaParcialDefensa
                delanteros.clear()
                delanteros.extend(sorted(delanterosParcial, key=lambda j: j.nombre))  # Ordenar los delanteros por nombre
                defensores.clear()
                defensores.extend(sorted(defensoresParcial, key=lambda j: j.nombre))  # Ordenar los defensores por nombre
                
            elif (sumaParcialAtaque == max_ataque) and (sumaParcialDefensa == max_defensa):
                print("entre")
                delanterosParcial = sorted(delanterosParcial, key=lambda j: j.nombre)
                if delanterosParcial > delanteros:
                    delanteros.clear()
                    delanteros.extend(delanterosParcial)  # Ordenar los delanteros por nombre
                    defensores.clear()
                    defensores.extend(sorted(defensoresParcial, key=lambda j: j.nombre))  # Ordenar los defensores por nombre
            return
        
        
        #caso "recursivo" 
        for j in range(len(jugadores)):
            jugadorN = jugadores[j]
            if jugadorN in usados:
                continue
            
            usados.append(jugadorN)
            delanterosParcial.append(jugadorN)
            i += 1

            backtracking(delanterosParcial, defensoresParcial, i, usados, delanteros, defensores)
            
            usados.remove(jugadorN)
            delanterosParcial.remove(jugadorN)
            i -= 1

    max_ataque = 0
    max_defensa = 0
    delanteros = []
    defensores = []

    backtracking([], [], 0, [], delanteros, defensores)

    return delanteros, defensores


def main():
    T = int(input());

    for case in range(1,T+1):
        jugadores: List[Jugador] = [];
        for _ in range(10):
            nombre, ataque, defensa = input().split();
            jugadorN = Jugador(nombre, int(ataque), int(defensa));
            jugadores.append(jugadorN);       
        delanteros, defensores = buscarFormacionIdeal(jugadores)
    
        print(f"Case {1}:")
        print(f"({', '.join(jugador.nombre for jugador in delanteros)})")
        print(f"({', '.join(jugador.nombre for jugador in defensores)})")
"""
def main():
    jugadores = [
    Jugador("sameezahur", 20, 21),
    Jugador("sohelh", 18, 9),
    Jugador("jaan", 17, 86),
    Jugador("sidky", 16, 36),
    Jugador("shamim", 16, 18),
    Jugador("shadowcoder", 12, 9),
    Jugador("muntasir", 13, 4),
    Jugador("brokenarrow", 16, 16),
    Jugador("emotionalblind", 16, 12),
    Jugador("tanaeem", 20, 97)
    ]
    hola = buscarFormacionIdeal(jugadores)
    for jugador in hola[0]:
        print(jugador.nombre)
"""
if __name__ == "__main__":
    main();