c = []

for _ in range(int(input())):
    a = list(map(int,input().split()))
    a.append(1)
    c.append(a)

for i in range(len(c)):
    for j in range(i+1,len(c)):
        if c[i][0] > c[j][0] and c[i][1] > c[j][1]:
            c[j][2] += 1
        elif c[i][0] < c[j][0] and c[i][1] < c[j][1]:
            c[i][2] += 1

for i in range(len(c)):
    print(c[i][2],end=' ')