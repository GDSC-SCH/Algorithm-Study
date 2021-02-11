# Dynamic Programming - 반복문을 이용한 Bottom-Up 방식

import sys

N = int(sys.stdin.readline())

dp = [None for _ in range(N + 1)]

dp[0] = dp[1] = 0

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])