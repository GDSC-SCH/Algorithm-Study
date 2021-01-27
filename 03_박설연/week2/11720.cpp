#include <iostream>
using namespace std;

int main()
{
   int n;
   int tmp;
   char c;
   int sum = 0;
   cin >> n;

    for (int i = 0; i < n; i++){
        cin >> c;
        tmp = c - '0'; //c- 48
        sum += tmp;
    }

    cout << sum << endl;

    return 0;
}
