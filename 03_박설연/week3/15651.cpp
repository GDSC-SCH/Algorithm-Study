#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector <int> v;

void se(int a) {
    if (a == m) {
        for (int i = 0; i < m; i++) {
            cout << v[i] << " ";
        }
        cout << "\n";
    }
    else {
        for (int j = 1; j <= n; j++) {
            v.push_back(j);
            se(a + 1);
            v.pop_back();
        }
    }
}
int main() {
    cin >> n >> m;
    se(0);
    return 0;
}