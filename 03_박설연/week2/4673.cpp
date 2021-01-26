//review 필요, (최종 수정 코드입니다.)

#include <iostream>
using namespace std;
bool arr[10001] = { false, };

int d(int n){
    int result = n;
    while (n!= 0){
        result += n % 10;
        n = n / 10;
    }

    return result;
}

int main(){
    int num;
    for (int i = 1; i <= 10000; i++){ //1부터 체크하도록 맞춰놓음
        num = d(i);
        if (num <= 10000)
            arr[num] = true;
    }

    for (int i = 1; i <= 10000; i++) {
        if (!arr[i])
            cout << i << endl;

    }
    return 0;
}
