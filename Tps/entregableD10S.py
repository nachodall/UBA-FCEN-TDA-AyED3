from typing import List;

class Jugador:
    def __init__(self, nombre, ataque, defensa):
        self.nombre = nombre;
        self.ataque = ataque;
        self.defensa = defensa;

def buscarFormacionIdeal(jugadores):
    print("entre")
    delanteros: List[Jugador] = [];
    defensores: List[Jugador] = [];
    max_ataque = 0;
    max_defensa = 0;
    i = 0;
    usados: List[Jugador] = [] # aca voy guardando los q probe como delantero


    def armarDefensores(usados):
        rta : List[Jugador] = [];
        for jugador in jugadores:
            if jugador not in usados:
                rta.append(jugador);
        return rta;


def buscarFormacionIdeal(jugadores):
    def armarDefensores(usados):
        return [jugador for jugador in jugadores if jugador not in usados]

    def backtracking(delanterosParcial, defensoresParcial, i, usados, max_ataque, max_defensa, delanteros, defensores):
        #caso base 
        if i == 5:
            defensoresParcial = armarDefensores(usados)
            sumaParcialAtaque = sum(jugador.ataque for jugador in delanterosParcial)
            sumaParcialDefensa = sum(jugador.defensa for jugador in defensoresParcial)

            if (sumaParcialAtaque > max_ataque) or ((sumaParcialAtaque == max_ataque) and (sumaParcialDefensa > max_defensa)):
                max_ataque = sumaParcialAtaque
                max_defensa = sumaParcialDefensa
                delanteros.clear()
                delanteros.extend(delanterosParcial)
                defensores.clear()
                defensores.extend(defensoresParcial)
                sorted(delanteros, key = lambda j: j.nombre);
                sorted(defensores, key = lambda j: j.nombre);
            return

        #caso "recursivo" 
        for j in range(len(jugadores)):
            jugadorN = jugadores[j]
            if jugadorN in usados:
                continue
            
            usados.append(jugadorN)
            delanterosParcial.append(jugadorN)
            i += 1

            backtracking(delanterosParcial, defensoresParcial, i, usados, max_ataque, max_defensa, delanteros, defensores)

            usados.remove(jugadorN)
            delanterosParcial.remove(jugadorN)
            i -= 1

    max_ataque = 0
    max_defensa = 0
    delanteros = []
    defensores = []

    backtracking([], [], 0, [], max_ataque, max_defensa, delanteros, defensores)

    return delanteros


def main():
    #T = int(input());

    #for k in range(1,T+1):
     #   jugadores: List[Jugador] = [];
      #  for _ in range(10):
       #     nombre, ataque, defensa = input().split();
        #    jugadorN = Jugador(nombre, int(ataque), int(defensa));
         #   jugadores.append(jugadorN);
        #buscarFormacionIdeal(jugadores);
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
    ];
    ta = buscarFormacionIdeal(jugadores); 
    for jugador in ta:
        print (jugador.nombre);

if __name__ == "__main__":
    main();