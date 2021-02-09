N, K = [int(x) for x in input().split()]

if N - K < K:
    K = N - K

ret = 1
for i in range(K):
    ret *= N - i
    ret //= i+1

print(ret)