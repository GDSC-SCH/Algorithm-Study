for _ in range(int(input())):
    
    a,b = map(int,input().split())

    up = 1
    down = 1

    for _ in range(a):
        up = up * b
        down = down * a
        b = b - 1
        a = a - 1

    print(up//down)