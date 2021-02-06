//처음으로 검색해본 알고리즘.. ㅠ

#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;

int DP[1002][1002];
string s1, s2;
int len1, len2;

int main(){
	cin >> s1 >> s2;
	
	//길이
	len1 = s1.size();
	len2 = s2.size();

	for (int i = 1; i <= len2; i++)
	{
		for (int j = 1; j <= len1; j++)
		{
			if (s2[i - 1] == s1[j - 1]) // 문자가 같으면 왼쪽 대각선 위
				DP[i][j] = DP[i - 1][j - 1] + 1;

			else // 문자가 다르면 왼쪽값과 위쪽값 비교
				DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]);
		}
	}

	cout << DP[len2][len1];
	return 0;
}
