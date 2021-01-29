N = int(input())

def hanoi(n, start, end):
    mid = 6 - start - end
    if n == 1:
        return [[start, end]]
    else:
        return hanoi(n-1, start, mid) + [[start, end]] + hanoi(n-1, mid, end)
    
result = hanoi(N, 1, 3)
print(len(result))
for a, b in result:
    print(a, b) 