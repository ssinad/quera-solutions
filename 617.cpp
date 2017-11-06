#include <iostream>
#include <algorithm>

using namespace std;

int palindrome(long long n){
    long long m = 0, tmp = n;
    while (tmp > 0) {
        m *= 10;
        m += tmp % 10;
        tmp /= 10;
    }
    return m;
}

int main(){
    long long n;
    cin >> n;
    if (n == palindrome(n)){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
}
