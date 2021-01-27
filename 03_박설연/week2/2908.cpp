#include <iostream>
#include <string>
using namespace std;

int main(){
	string a, b, s;
	cin >> a >> b;

	for(int i = 2; i >= 0; i--){
		if(a[i] > b[i]){
			s = a; 
			break;
		}
		else if(a[i] < b[i]) {
			s = b; 
			break;
		}
	}

	for (int i = 2; i >= 0; i--)
		cout << s[i];
	cout << endl;
	return 0;
}
