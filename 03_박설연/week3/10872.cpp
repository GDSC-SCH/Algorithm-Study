#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	int tmp = 1;
	for (int i = 1; i <= N; i++) {
		tmp *= i;
	}
	cout << tmp;

	return 0;
}