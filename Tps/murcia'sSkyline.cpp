//Consigna: https://vjudge.net/problem/UVA-11790

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void calculateSkyline(int caseNum, int n, vector<int>& heights, vector<int>& widths) {
    vector<int> increasingPartial(n, 0); //Aca se guarda la long de la subseq creciente mas larga hasta que termina la pos i
    vector<int> decreasingPartial(n, 0);

    for (int i = 0; i < n; i++) {
        increasingPartial[i] = widths[i]; // inicializamos con su ancho a cada edificio
        for (int j = 0; j < i; j++) {
            if (heights[i] > heights[j]) {
                increasingPartial[i] = max(increasingPartial[i], increasingPartial[j] + widths[i]);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        decreasingPartial[i] = widths[i];
        for (int j = 0; j < i; j++) {
            if (heights[i] < heights[j]) {
                decreasingPartial[i] = max(decreasingPartial[i], decreasingPartial[j] + widths[i]);
            }
        }
    }

    int increasing = *max_element(increasingPartial.begin(), increasingPartial.end()); //devuelvo el value del max
    int decreasing = *max_element(decreasingPartial.begin(), decreasingPartial.end());

    cout << "Case " << caseNum << ". ";
    if (increasing >= decreasing) {
        cout << "Increasing (" << increasing << "). Decreasing (" << decreasing << ")." << endl;
    } else {
        cout << "Decreasing (" << decreasing << "). Increasing (" << increasing << ")." << endl;
    }
}

int main() {
    int testCases;
    cin >> testCases;
    
    for (int i = 1; i <= testCases; ++i) {
        int n;
        cin >> n;
        
        vector<int> heights(n);
        vector<int> widths(n);
        
        for (int j = 0; j < n; ++j) {
            cin >> heights[j];
        }
        
        for (int j = 0; j < n; ++j) {
            cin >> widths[j];
        }
        
        calculateSkyline(i, n, heights, widths);
    }
    
    return 0;
}

