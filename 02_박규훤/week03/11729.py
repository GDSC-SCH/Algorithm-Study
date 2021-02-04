N = int(input())

def hanoi(n, start, end):
    mid = 6 - start - end
    if n == 1:
        return ((start, end),)
    return hanoi(n-1, start, mid) + ((start, end),) + hanoi(n-1, mid, end)

ret = hanoi(N, 1, 3)
print(len(ret))
for a, b in ret:
    print(a, b)