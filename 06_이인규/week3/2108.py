import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]

print("%.f" % (sum(lst)/N))

lst.sort()

print(lst[N//2])

import collections

collect = collections.Counter(lst).most_common()

if len(collect) > 1:
    if collect[0][1] == collect[1][1]:
        print(collect[1][0])
    else:
        print(collect[0][0])
else:
    print(lst[0])

print(lst[N-1] - lst[0])