#include <iostream>
// #include <algorithm>

using namespace std;

long double myPow(long double base, unsigned int exp){
    if (base == 0 || base == 1){
        return base;
    }
    if (exp == 0){
        return 1;
    }
    return base * myPow(base, exp - 1);
}

int main(){
    long double base, result;
    unsigned int exp;
    cin >> base >> exp;
    // cout << myPow(base, exp);
    printf("%.3Lf", myPow(base, exp));
    return 0;
}
