#include <iostream>
using namespace std;

int main() {
	int x, y;
	int a, b, c, d;
	cin >> x;
	cin >> y;
	a = x * ((y % 100) % 10);
	b = x * ((y % 100) / 10);
	c = x * (y / 100);
	d = x * y;
	cout << a << endl << b << endl << c << endl << d << endl;

	return 0;
}
