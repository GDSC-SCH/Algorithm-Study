import sys

input = sys.stdin.readline

N = int(input())

is_prime = [False, False] + [True] * (N-1)

for n in range(2, N+1):
    if is_prime[n]:
        for i in range(n*2, N+1, n):
            is_prime[i] = False

primes = [i for i, p in enumerate(is_prime) if p]

# i번째 소수까지의 합
# 연속되는 소수들의 합으로 이루어져 있으므로
# sums[15] - sums[10] = N 이면 primes[11]부터 primes[15]까지의 합이 N
sums = [0] * (len(primes)+1)
for i in range(len(primes)):
    sums[i+1] = sums[i] + primes[i]

answer = 0
start, end = 0, 1

while start < len(sums):
    if sums[end] - sums[start] == N:
        answer += 1
        start += 1
    elif sums[end] - sums[start] > N:
        start += 1
    elif end < len(sums) - 1:
        end += 1
    else:
        start += 1

print(answer)