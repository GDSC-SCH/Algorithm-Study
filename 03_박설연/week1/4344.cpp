#include <iostream>
using namespace std;

int main() {
	int C, N, num;
	int avg;
	int score[1000] = { 0, };
	double result;

	cin >> C;
	for (int i = 0; i < C; i++) {
		avg = 0;
		num = 0;
		cin >> N;

		for (int j = 0; j < N; j++) {
			cin >> score[j];
			avg += score[j];
		}
		avg = avg / N;
		for (int j = 0; j < N; j++) {
			if (score[j] > avg)
				num++;
		}
		result = (double)num / N * 100;

		cout << fixed;
		cout.precision(3);
		cout << result << "%" << endl;
	}
}
