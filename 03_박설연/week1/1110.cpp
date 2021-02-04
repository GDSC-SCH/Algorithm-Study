#include <iostream>
using namespace std;

int main()
{
	int num;
	int a, b, c, d;

	cin >> num;
	a = num;
	int count = 0;


	while (1) {
		b = a / 10;
		c = a % 10; 

		d = b + c; 

		d = d%10; 
		a = ((c * 10) + d);
		count += 1;

		if (((c * 10) + d) == num)
			break;
	}
	cout << count;
}
