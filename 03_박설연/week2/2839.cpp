#include <iostream>
using namespace std;


int main(){
    int N;
    int count = 0;
    
    cin >> N;

    while (1){
		
		if (N % 5 == 0){
			count+= N / 5;
			break;
		}
		else if (N % 3 == 0) {
			N = N - 3;
			count++;
		}
		else if (N > 5){
			N -= 5;
			count++;
		}
		else {
			count = -1;
			break;
		}

		
    }
	cout << count << endl;
	return 0;
}