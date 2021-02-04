#include <iostream>
using namespace std;

int h[15][15] = { 0, };

int main(){
	for (int i = 0; i < 15; i++) 
		h[0][i] = i;

	for (int i = 1; i < 15; i++) {
		int sum = 0;
		for (int j = 1; j < 15; j++) {
			
			h[i][j] += sum + h[i - 1][j];
			sum += h[i - 1][j];
		}
	}

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int k, n;
		cin >> k >> n;
		cout << h[k][n] << endl;
	}
	return 0;
}
