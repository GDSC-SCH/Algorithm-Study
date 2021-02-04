#include <iostream>
using namespace std;

int main() {
	int a;
	int T[10] = { 0, };
	int count = 0;

	for (int i = 0; i < 10; i++) {
		cin >> a;
		T[i] = a % 42;
		for (int j = 0; j <= i; j++) {
			if ((i != j) && (T[i] == T[j])) {
				count--;
				break;
			}
		}
		count++;
	}
	cout << count << endl;
	return 0;
}