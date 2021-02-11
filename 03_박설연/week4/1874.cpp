#include<iostream>
#include<vector>
#include<string.h>
using namespace std;

int n;
int cnt = 0;
int seq[100001];
vector<int> v;
vector<char> pm;

int main(){
	cin >> n;
	for (int i = 0; i < n; i++) 
		cin >> seq[i];

	for (int i = 1; i <= n; i++){
		v.push_back(i);
		pm.push_back('+');


		while (!v.empty() && v.back() == seq[cnt]){
			v.pop_back();
			pm.push_back('-');
			cnt++;
		}
	}

	if (!v.empty()) cout << "NO";
	else {
		for (int i = 0; i < pm.size(); i++)
			cout << pm[i] << endl;
	}

}