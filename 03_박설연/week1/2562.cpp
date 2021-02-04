#include <iostream>
using namespace std;

int main() {
	int T[100];
	int max = 0; int num = 0;
	for (int i = 0; i < 9; i++) {
		cin >> T[i];

		if (max < T[i]) {
			max = T[i];
			num = i+1;
		}
	}
	cout << max << endl << num;

}