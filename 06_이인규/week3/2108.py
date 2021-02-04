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

count = 0; win = 0; e = []
for i in c:
    count = c.count(i)
    if count > win:
        win = count
        del e[0:len(e)-1]
        e.append(i)
    elif count == win:
        e.append(i)

k = list(set(e))
k.sort()

if len(k) > 1:
    print(k[1])
else:
    print(*k)
print(max(c)-min(c))