//resuelto de honi

#include <math.h>
#include <string>
#include <vector>

using namespace std;

const int OP_ADD = 0;
const int OP_MUL = 1;
const int OP_POW = 2;
vector<string> ops = {"+", "×", "↑"};

vector<vector<vector<int>>> memo;

vector<int> f(vector<int> v, int w, int i) {
    // Verifica si no hay elementos en el vector y w es 0
    if (v.size() == 0 && w == 0) return {};
    // Si solo hay un elemento en el vector y w es igual al elemento, no se necesitan operaciones
    if (i == 0) {
        if (w == v[0]) return {};
        else return {-1};
    }
    // Si w es negativo, no es posible obtener w con los elementos restantes
    if (w < 0) return {-1};

    // Si el resultado para el estado actual no está memoizado
    if (memo[w][i].size() == 0) {
        vector<int> res;

        // Operación: suma
        res = f(v, w - v[i], i - 1);
        if (res.size() == 0 || res[0] != -1) {
            res.push_back(OP_ADD);
            memo[w][i] = res;
            return res;
        }

        // Operación: multiplicación
        if (w % v[i] == 0) {
            res = f(v, w / v[i], i - 1);
            if (res.size() == 0 || res[0] != -1) {
                res.push_back(OP_MUL);
                memo[w][i] = res;
                return res;
            }
        }

        // Operación: potencia
        float x = pow(w, 1.0 / v[i]);
        if (fmod(x, 1.0) == 0) {
            res = f(v, x, i - 1);
            if (res.size() == 0 || res[0] != -1) {
                res.push_back(OP_POW);
                memo[w][i] = res;
                return res;
            }
        }

        // Si ninguna operación es posible, marca este estado como inválido
        memo[w][i] = {-1};
    }

    // Retorna el resultado memoizado para este estado
    return memo[w][i];
}


int main(int argc, char *argv[]) {
    // Parse input.
    int w = atoi(argv[1]);
    int n = atoi(argv[2]);
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        v[i] = atoi(argv[3 + i]);
    }

    // Print input.
    printf("w: %d\n", w);
    printf("v: [");
    for (int i = 0; i < v.size(); i++) {
        printf("%d", v[i]);
        if (i < v.size() - 1) printf(", ");
    }
    printf("]\n");

    // Calculate solution.
    memo = vector<vector<vector<int>>>(w + 1, vector<vector<int>>(v.size()));
    vector<int> res = f(v, w, v.size() - 1);

    // Print solution.
    if (res.size() == 1 && res[0] == -1) {
        printf("no solution available\n");
    } else if (res.size() == 0) {
        printf("solution: no operations required\n");
    } else {
        printf("solution: ");
        for (int i = 0; i < res.size(); i++) printf("(");
        printf("%d", v[0]);
        for (int i = 0; i < res.size(); i++) {
            printf(" %s", ops[res[i]].c_str());
            printf(" %d)", v[i + 1]);
        }
        printf("\n");
    }

    return 0;
}