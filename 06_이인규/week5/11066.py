# 왜 안되는가...

for _ in range(int(input())):
    lst = []
    a = int(input())

    for i in range(a):
        lst = list(map(int,input().split()))

    for __ in range(a-1):
        min = lst[0] + lst[1]
        dex = 0
        sum = 0

        for i in range(1,len(lst)-1):
            if min > (lst[i] + lst[i+1]):
                min = lst[i] + lst[i+1]
                dex = i
        sum += min
        lst[dex] = 0; lst[dex+1] = 0
        lst.remove(0)
    print(sum)