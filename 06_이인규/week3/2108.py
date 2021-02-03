c = []
d = []

for _ in range(int(input())):
    a = int(input())
    c.append(a)
    d.append(a)

print(round(sum(c)//len(c),0))

cnt = len(c)//2

for _ in range(cnt):
    d.remove(max(d))
    d.remove(min(d))

print(*d)

e = []
for i in c:
    if i not in e:
        toss = [i,1]
        e.append(toss)
    else:
        e[e.index(i)][1] += 1

print(e)

print(max(c)-min(c))

# 푸는중