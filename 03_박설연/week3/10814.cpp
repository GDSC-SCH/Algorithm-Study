#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


pair<int, string> arr[100001];
int n, s, ag;
string name;

//
bool comp(pair<int, string> a, pair<int, string> b) {
    if (a.first < b.first) return true;
    return false;
}


int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> ag >> name;
        arr[i] = make_pair(ag, name);
    }

    stable_sort(arr, arr + n, comp);

    for (int i = 0; i < n; i++)
        cout << arr[i].first << ' ' << arr[i].second << endl;
}