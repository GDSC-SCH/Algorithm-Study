
//**중요
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


vector<int> num;
vector<int> res;
vector<int> op;


int n;
int oper[4] = { 0, };


int calculator(){
    int sum = num[0];
    for (int i = 0; i < n - 1; i++) {
        int x = op[i];
        if (x == 0) {
            sum += num[i + 1];
        }
        else if (x == 1) {
            sum -= num[i + 1];
        }
        else if (x == 2) {
            sum *= num[i + 1];
        }
        else {
            sum /= num[i + 1];
        }
    }

    return sum;
}

void dfs(int cnt) {
    if (cnt == n - 1) {
        int sum = calculator();
        res.push_back(sum);
        return;
    }

    for (int i = 0; i < 4; i++) {
        if (oper[i]) {
            oper[i]--;
            op.push_back(i);

            dfs(cnt + 1);

            oper[i]++;
            op.pop_back();
        }
    }
}

int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        num.push_back(x);
    }

    for (int i = 0; i < 4; i++)
        cin >> oper[i];

    dfs(0);
     sort(res.begin(), res.end());
    cout << res.back() << endl << res[0];

}