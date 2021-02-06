#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;


int n;
vector<int> arr;
int pos[4001], neg[4001];

double average() {
    int sum = 0;
    for (int i = 0; i < n; i++) 
        sum += arr[i];

    double d_sum = sum;
    return round(d_sum / n);
}

int median() {
    return arr[n / 2];
}

int mode() {
    int max_cnt = -1;
    vector<int> amode;
    for (int i = 0; i < n; i++){
        if (arr[i] < 0){
            neg[abs(arr[i])]++;
        }
        else{
            pos[arr[i]]++;
        }
    }
    for (int i = 0; i <= 4000; i++) {
        if (pos[i] > max_cnt) max_cnt = pos[i];
        if (neg[i] > max_cnt) max_cnt = neg[i];
    }
    for (int i = 0; i <= 4000; i++) {
        if (pos[i] == max_cnt) amode.push_back(i);
        if (neg[i] == max_cnt) amode.push_back(i * (-1));
    }
    
    if (amode.size() == 1) return amode[0];

    sort(amode.begin(), amode.end());
    
    return amode[1];
}

int range(){
    return arr[n - 1] - arr[0];
}

int main() {
    //속도 처리
    cin.tie(NULL);
    ios::sync_with_stdio(false);


    cin >> n;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end());
    cout << average() << endl;
    cout << median() << endl;
    cout << mode() << endl;
    cout << range();
    return 0;
}
