for _ in range(int(input())):
    a,index_Q = map(int,input().split())
    lst = list(map(int,input().split()))
    count = 0

    if max(lst) == lst[0]:
        if index_Q == 0:
            count += 1
            break
        del lst[0]
        count += 1
    
    elif index_Q != 0:
        lst.append(lst[0])
        del lst[0]
    
    else:
        