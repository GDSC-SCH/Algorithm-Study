# 하는 중

a = []

for _ in range(int(input())):
    ll,num = input().split()
    num = int(num)
    
    if ll == 'push':
        a.append(num)
    if ll == 'pop':
        if len(a) == 0:
            print(-1)
        else:
            print(len(a)-1)
            a.pop()
    if ll == 'size':
        print(len(a))
    if ll == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)
    if ll == 'top':
        if len(a) == 0:
            print(-1)
        else:
            print(a[len(a)-1])