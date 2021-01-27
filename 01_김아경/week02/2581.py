M = int(input())
N = int(input())

prime = [True for _ in range(N+1)]
prime[0] = False
prime[1] = False

for i in range(2, N+1):
    if prime[i]:
        j = 2
        while i*j <= N:
            prime[i*j] = False
            j += 1

result = []
for i in range(M, N+1):
    if prime[i]:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)