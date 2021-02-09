#include <iostream>
#include <vector>
using namespace std;

int main(){
    //1)종류랑 총 액수 입력 받기
    int N, K;    
    cin >> N >> K;

    //2)int형 벡터 선언, 동전 요소 넣기
    int A;    
    vector<int> value;
    for(int i = 0; i < N; i++){
        cin >> A;
        value.push_back(A);
    }

    //3) 큰 수부터 비교, 나누어준다.
    int c = 0;
    for(int i = N - 1; i >= 0; i--){
       if(K / value[i] > 0){
            c += (K / value[i]);
            K %= value[i];
        }
    }
    cout << c;
    return 0;
}
