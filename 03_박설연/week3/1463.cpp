#include<iostream>
using namespace std;
int a[1000000];

int F(int n) {
	a[1] = 0;
	for (int i = 2; i <= n; i++) {
		a[i] = a[i - 1] + 1;
		if (i % 2 == 0 && a[i] > a[i / 2] + 1) {
			a[i] = a[i / 2] + 1;
		}
		if (i % 3 == 0 && a[i] > a[i / 3] + 1) {
			a[i] = a[i / 3] + 1;
		}
	}
	return a[n];
}

int main() {
	int t;
	cin >> t;
	cout << F(t) << endl;
}