N = int(input())
P = [int(x) for x in input().split()]

P.sort()
ret = 0
for i in range(1, N+1):
    ret += sum(P[:i])

print(ret)