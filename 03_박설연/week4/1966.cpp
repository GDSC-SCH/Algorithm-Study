#include <iostream>
#include <queue>
using namespace std;

int main(){
	int T;
	cin >> T;

	while (T) {
		priority_queue<int> pq;
		queue<pair<int, int>> q;
		//수와 위치를 나타내는 변수
		int N, M; 
		int max = 0;
		int n = 0;

		cin >> N >> M;

		//중요도를 두 큐에 저장합니다.
		for (int i = 0; i < N; i++) {
			int x;
			cin >> x;
			pq.push(x);
			q.push(pair<int, int>(i, x));
		}

		//값 비교
		while (!pq.empty()){
			if (pq.top() != q.front().second) {
				pair<int, int> p = q.front();
				q.pop();
				q.push(p);
			}
			//값과 첫번째 비교하여, 출력 순서 출력
			else{
				if(M == q.front().first){ 
					cout << n + 1 << endl; 
					break;
				}
				else {
					pq.pop();
					q.pop();
					n++;
				}
			}
		}
		T--;
	}
}