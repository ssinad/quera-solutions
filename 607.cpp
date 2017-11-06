#include <iostream>
// #include <algorithm>

using namespace std;



int main(){
    
    unsigned int p, q, r;
    cin >> p >> q >> r;
    int **m1, **m2, **result;
    // cout << myPow(base, exp);
    
    m1 = new int*[p];
    for (int i = 0; i < p; i++) {
        m1[i] = new int[q];
        for (int j = 0; j < q; j++) {
            cin >> m1[i][j];
        }
    }
    
    m2 = new int*[q];
    for (int i = 0; i < q; i++) {
        m2[i] = new int[r];
        for (int j = 0; j < r; j++) {
            cin >> m2[i][j];
        }
    }
    
    result = new int*[p];
    for (int i = 0; i < p; i++) {
        result[i] = new int[r];
        for (int j = 0; j < r; j++) {
            int sum = 0;
            for (int k = 0; k < q; k++) {
                sum += m1[i][k] * m2[k][j];
            }
            result[i][j] = sum;
            cout << sum << " ";
        }
        cout << endl;
    }
    
    return 0;
}
