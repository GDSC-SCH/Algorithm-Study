//복습 체크
#include <iostream>
using namespace std;


int main(){
    int M, N;
    int MIN;
    int sum = 0;


    cin >> M >> N;
    MIN = N;

    for (int i = M; i <= N; i++){
        for (int j = 2; j <= i; j++){
            if (i % j != 0){
                if (j == i - 1){
                    sum += i;
                    if (i < MIN)
                        MIN = i;
                }
            }
            else{
                if (i == 2) {
                    MIN = 2;
                    sum += 2;
                }
                break;
            }
        }
    }

    if (sum == 0)
        cout << -1;
    else
        cout << sum << endl << MIN << endl;
}