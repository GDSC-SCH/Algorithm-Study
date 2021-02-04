//함수 구현 알고리즘

#include <iostream>
#include <vector>
using namespace std;

long long sum(vector<int>& a) {
	long long num = 0;

	for (int i = 0; i < a.size(); i++) {
		num += a[i];
	}
	return num;
}
