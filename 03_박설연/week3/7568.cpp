#include <iostream>
#include <vector>
using namespace std;

typedef struct {
	int X;
	int Y;
}Inform;


int main(void) {
	int N;

	cin >> N;
	Inform arr[51];

	for(int i = 0; i < N; i++) {
		int X, Y;
		cin >> X >> Y;
		arr[i].X = X;
		arr[i].Y = Y;
	}



	for (int i = 0; i < N; i++){
		int ans= 0;
		for(int j = 0; j < N; j++){
			if ((arr[i].X < arr[j].X) && (arr[i].Y < arr[j].Y))
				ans++;
		}

		cout << ans + 1 << " ";
	}

}
