# 하는중

for _ in range(int(input())):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    
    count = 1
    target_index = b

    while 1:
        c_max = max(c)
        number = c[0]
        del c[0]

        if number == c_max and target_index == 0:
            count += 1
        else:
            c.append(number)
        if len(c) == 0:
            break

    print(count)