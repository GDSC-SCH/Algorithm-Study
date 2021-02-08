def gob(n):
    sum=1
    for i in range(1, n+1):
        sum = sum * i
    return sum


N, K = map(int, input().split())

print(int(gob(N)/(gob(K)*gob(N-K))))