#include <iostream>
using namespace std;

long long P(long long a, long long b, long long c) {
    if (b == 0) {
        return 1;
    }
    else if (b == 1) {
        return a % c;
    }
    long long tmp = P(a, b / 2, c);
    tmp = (tmp * tmp) % c;
    //분할하여 계산 하기(재귀를 통한)
    //B가 짝수일 때
    if (b % 2 == 0) 
        return tmp;
    //B가 홀수일 때
    else 
        return tmp * a % c;
}

int main(){
    long long A, B, C;
    cin >> A >> B >> C;
    cout << P(A, B, C) << endl;
}
