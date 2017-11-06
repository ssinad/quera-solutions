//
//  297.cpp
//  
//
//  Created by SS D on 2017-08-22.
//
//

#include <iostream>

using namespace std;

int main(){
    double sum = 1;
    int n;
    double x, num = 1, den = 1;
    cin >> x >> n;
    
    for (int cnt = 1; cnt < n; ++cnt) {
        num *= x;
        den *= cnt;
        sum += num / den;
    }
    printf("%.3lf", sum);
    return 0;
}
