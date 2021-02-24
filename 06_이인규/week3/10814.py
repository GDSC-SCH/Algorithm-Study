lst = []

for i in range(int(input())):
    a,b = map(str,input().split())
    lst.append([int(a)+i/1000000,b])

lst.sort()

for i in range(len(lst)):
    print(int(lst[i][0]),lst[i][1])