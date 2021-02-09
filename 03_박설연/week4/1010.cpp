#include <iostream>
using namespace std;

//재귀로 풀어보기
long long c(int n, int r) {
    static long long d[30][30] = { 0, };
    if (d[n][r] > 0) 
       return d[n][r];
    if (r == 0 || n == r)
       return d[n][r] = 1;
    return d[n][r] = c(n - 1, r - 1) + c(n - 1, r);
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        int N, M;
        cin >> N >> M;

        printf("%lld\n", c(M, N));
    }

    return 0;
}
