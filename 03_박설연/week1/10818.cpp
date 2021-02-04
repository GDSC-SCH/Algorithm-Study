#include <iostream>
using namespace std;
int T[1000001];
int N;
int min = 1000000;
int max = -1000000;

int main() {
	
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> T[i];
		if (T[i] <= min) {
			min = T[i];
		}
		if (T[i] >= max)
			max = T[i];
	}
	cout << min << " " << max;
	return 0;

}