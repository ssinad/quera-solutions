#include <iostream>

using namespace std;

int main(){
    // long long sum = 0;
    double sum = 0;
    int m, n;
    cin >> n >> m;
    for (int i = -10; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            sum += (i + j) * (i + j) * (i + j) / j / j * 1.0;
        }
    }
    cout << sum << endl;
    return 0;
}
