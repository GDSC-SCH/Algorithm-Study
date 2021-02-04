n_prime = 10001
prime = [False, False] + [True] * (n_prime-2)

for i in range(2, n_prime):
    if prime[i]:
        num = i * 2
        while num < n_prime:
            prime[num] = False
            num += i
M, N = [int(input()) for _ in range(2)]
ret = [i for i in range(M, N+1) if prime[i]]
if ret:
    print(sum(ret))
    print(min(ret))
else:
    print(-1)