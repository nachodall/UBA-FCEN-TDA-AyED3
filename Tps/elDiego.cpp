//consigna: vjudge.net/problem/UVA-11804

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Player { //creamos player para representar a cada jugador
public:
    string name;
    int attack;
    int defense;

    Player(const string& name, int attack, int defense) : name(name), attack(attack), defense(defense) {}

    string getName() const {
        return name;
    }

    int getAttSum() const {
        return attack;
    }

    int getDefSum() const {
        return defense;
    }
};

vector<string> bestForwards;
vector<string> bestDefenders;
int bestAttackSum = 0;
int bestDefenseSum = 0;

bool lexSmaller(const vector<string>& list1, const vector<string>& list2) { //compara dos str
    for(size_t i = 0; i < list1.size(); i++) {
        int comparisonValue = list1[i].compare(list2[i]);
        if(comparisonValue < 0) {
            return true;
        } else if (comparisonValue > 0){
            return false;
        }
    }
    return false;
}

int sumAtt(const vector<Player>& players) {
    int sum = 0;
    for (const Player& player : players) {
        sum += player.getAttSum();
    }
    return sum;
}

int sumDef(const vector<Player>& players) {
    int sum = 0;
    for (const Player& player : players) {
        sum += player.getDefSum();
    }
    return sum;
}

void backtracking(int i, int j, const vector<Player>& currentDefenders, const vector<Player>& currentForwards, const vector<Player>& players) {
    if (i == 5 && j == 5) { //llenamos ambos equipos 
        int attackSum = sumAtt(currentForwards);
        int defenseSum = sumDef(currentDefenders);
        
        vector<string> currentForwardNames;
        for(const Player& forward : currentForwards) {
            currentForwardNames.push_back(forward.getName());
        }
        sort(currentForwardNames.begin(), currentForwardNames.end()); //ordenamos los delaneros
        
        //vemos todos los casos que pueden suceder
        if (attackSum > bestAttackSum || (attackSum == bestAttackSum && defenseSum > bestDefenseSum) || (attackSum == bestAttackSum && defenseSum == bestDefenseSum && lexSmaller(currentForwardNames, bestForwards))) {
            bestAttackSum = attackSum;
            bestDefenseSum = defenseSum;

            bestForwards.clear();
            for (const Player& player : currentForwards) {
                bestForwards.push_back(player.getName());
            }
            sort(bestForwards.begin(), bestForwards.end());

            bestDefenders.clear();
            for (const Player& player : currentDefenders) {
                bestDefenders.push_back(player.getName());
            }
            sort(bestDefenders.begin(), bestDefenders.end());
        }
        return;
    }

    size_t playerIndex = i + j;

    //bt actualizando delanteros y defensores
    if (i < 5) {
        vector<Player> updatedForwards = currentForwards;
        updatedForwards.push_back(players[playerIndex]);
        backtracking(i + 1, j, currentDefenders, updatedForwards, players);
    }
    if (j < 5) {
        vector<Player> updatedDefenders = currentDefenders;
        updatedDefenders.push_back(players[playerIndex]);
        backtracking(i, j + 1, updatedDefenders, currentForwards, players);
    }
}

//choclo de codigo para parsear input y output
int main() {
    int T;
    cin >> T;
    cin.ignore();
    
    for (int test = 0; test < T; test++) {
        vector<Player> players;
        for (int i = 0; i < 10; i++) {
            string name;
            int attack, defense;
            cin >> name >> attack >> defense;
            players.emplace_back(name, attack, defense);
        }
        backtracking(0, 0, vector<Player>(), vector<Player>(), players);
        cout << "Case " << (test + 1) << ":" << endl;
        cout << "(" << bestForwards[0];
        for (size_t i = 1; i < bestForwards.size(); ++i) {
            cout << ", " << bestForwards[i];
        }
        cout << ")" << endl;
        cout << "(" << bestDefenders[0];
        for (size_t i = 1; i < bestDefenders.size(); ++i) {
            cout << ", " << bestDefenders[i];
        }
        cout << ")" << endl;
        bestForwards.clear();
        bestDefenders.clear();
        bestAttackSum = 0;
        bestDefenseSum = 0;
    }
    return 0;
}
