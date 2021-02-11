#include <iostream>
#include <deque>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;
	deque<int> dq;

	int arr[51];
	//찾는 수
	for (int i = 0; i < M; i++) {
		int a;
		cin >> a;
		arr[i] = a;
	}

	//큐 만들기
	for (int i = 1; i <= N; i++) {
		dq.push_back(i);
	}

	int idx = 0;
	int sum = 0;

	while (idx < M) {
		//임시큐
		deque<int> temp;
		int left = 0;
		int right = 0;

		// 왼쪽으로 이동
		while (1) {
			if (dq.front() == arr[idx]) 
				break;
			temp.push_back(dq.front());
			dq.pop_front();
			left++;
		}
		// 다시
		while (temp.size() != 0) {
			dq.push_front(temp.back());
			temp.pop_back();
		}

		// 오른쪽으로 이동하기
		while (1){
			if (temp.size() != 0 && temp.front() == arr[idx]) 
				break;
			int back = dq.back();
			dq.pop_back();
			right++;

		
			temp.push_front(back);
		}

		while (temp.size() != 0) {
			dq.push_back(temp.front());
			temp.pop_front();
		}
		//왼쪽
		if (left < right) {
			sum += left;
			

			while (left) {
				int temp = dq.front();
				dq.pop_front();
				dq.push_back(temp);
				left--;
			}
			dq.pop_front();
		}
		//오른쪽
		else {
			sum += right;
			
			while (right) {
				int temp = dq.back();
				dq.pop_back();
				dq.push_front(temp);
				right--;
			}
			dq.pop_front();
		}

		idx++;
	}

	cout << sum << endl;
	return 0;
}