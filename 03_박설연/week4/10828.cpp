#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;


int main(){
	int N;
	cin >> N;
	stack<int> Stack;
	for (int i = 0; i < N; ++i){
		string s;
		cin >> s;

		if (s == "push"){
			int n;
			cin >> n;
			Stack.push(n);
		}

		else if(s == "pop"){
			if (Stack.empty())
				cout << -1 << endl;
			else{
				cout << Stack.top() << endl;
				Stack.pop();
			}
		}


		else if (s == "size"){
			cout << Stack.size() << endl;
		}

		else if (s == "empty"){
			if (Stack.empty())
				cout << 1 << endl;
			else
				cout << 0 << endl;
		}

		else if (s == "top") {
			if (Stack.empty())
				cout << -1 << endl;
			else {
				cout << Stack.top() << endl;

			}
		}
	}
}