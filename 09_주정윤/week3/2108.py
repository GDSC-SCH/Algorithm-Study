import sys

N = int(input())
list = []
for i in range(N):
    list.append(int(sys.stdin.readline()))

a = sum(list)/N
a = round(a)
print(a)

list.sort()
num = N//2
mid = list[num]
print(mid)

from collections import Counter

count_num = Counter(list)

most = count_num.most_common()

if len(list) > 1:
    if most[0][1] == most[1][1]:
        mod = most[1][0]

    else:
        mod = most[0][0]
else:
    mod = most[0][0]
print(mod)

print(max(list) - min(list))