data = [[int(x) for x in input().split()] for _ in range(int(input()))]

ret = []
for d1 in data:
    count = 1
    for d2 in data:
        if d1 == d2:
            continue
        if d1[0] < d2[0] and d1[1] < d2[1]:
            count += 1
    ret.append(str(count))

print(' '.join(ret))