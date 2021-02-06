N, K = [int(x) for x in input().split()]
coins = [int(input()) for _ in range(N)]
cnt = 0

for c in coins[::-1]:
    n = K // c
    K -= c * n
    cnt += n

print(cnt)