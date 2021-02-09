#include <iostream>
#include <algorithm>
using namespace std;
const int MAX = 1000;


int main(){
    int N;
    int p[MAX];
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> p[i];
    sort(p, p + N);
    int sum = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j <= i; j++)
            sum += p[j];
    cout << sum << endl;
    return 0;
}
