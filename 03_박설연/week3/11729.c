#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)


void hanoi(int n, int s, int m, int e)
{
    if (n == 1)
    {
        printf("%d %d\n", s, e);
        return;
    }
    hanoi(n - 1, s, e, m);
    hanoi(1, s, m, e);
    hanoi(n - 1, m, s, e);
}

int main()
{
    int N;
    scanf("%d", &N);

    int K = pow(2, N) - 1;
    printf("%d\n", K);
    hanoi(N, 1, 2, 3);

    return 0;
}