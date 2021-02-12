import sys

N, K = map(int, sys.stdin.readline().split())

coin = []
for i in range(N):
    c = int(sys.stdin.readline())
    coin.append(c)

result = 0
for i in reversed(range(N)):
    result += K // coin[i]
    K %= coin[i]

print(result)