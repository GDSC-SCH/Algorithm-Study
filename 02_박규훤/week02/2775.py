N = int(input())

for _ in range(N):
    k = int(input())
    n = int(input())
    floor = [i for i in range(n+1)]
    for _ in range(k):
        floor = [sum(floor[:i+1]) for i in range(n+1)]
    print(floor[n])