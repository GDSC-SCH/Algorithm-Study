#include <iostream>
using namespace std;

//내가 이항계수 계산할 때 공식으로 풀어보기
int main() {
	int  N, K;
	cin >> N >> K;


	int result = 1;
	int a = 1;

	for (int i = N; i > N-K; i--) {
		result *= i;
	}

	for (int i = 1; i <= K; i++) {
		a *= i;
	}

	cout << (result / a);

	return 0;
}