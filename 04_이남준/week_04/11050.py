import sys

N, K = map(int, sys.stdin.readline().split())

nf = {0: 1} # 0! = 1

result = 1
for i in range(1, N+1):
    result *= i
    nf[i] = result # 팩토리얼 계산 후 저장

# 이항계수(N K) 구하는 공식 = N! / (K! * (N - K)!)
print(nf[N] // (nf[K] * nf[N-K]))