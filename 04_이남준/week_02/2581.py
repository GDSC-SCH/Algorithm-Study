def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


M = int(input())
N = int(input())

prime = []
sum = 0
for i in range(M, N + 1):
    if is_prime(i):
        prime.append(i)
        sum += i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(prime[0])