#include<iostream>
#include <string>
using namespace std;

int main() {
	string s;
	int arr[26] = { 0, };
	int MAX = 0;
	char c;
	
	cin >> s;

	
	for(int i = 0; i < s.length(); i++){
		if(s[i] >= 'A' && s[i] <= 'Z')
			arr[s[i] - 65] += 1; //숫자로 표현하기(아스키)
		else if (s[i] >= 'a' && s[i] <= 'z')
			arr[s[i] - 97] += 1;
	}
	
	for(int i = 0; i < 26; i++){
		if(arr[i] > MAX) {
			MAX = arr[i];
			c = i + 65;
		}
		else if (arr[i] == MAX){
			c = '?';
		}
	}

	cout << c << endl;

	return 0;
}