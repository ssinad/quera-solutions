#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    int m = max(max(a, b), c);
    if (a * a + b * b + c * c == 2 * m * m) {
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
}
