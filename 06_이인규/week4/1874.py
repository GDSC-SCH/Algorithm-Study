num = int(input())
lst = [int(input()) for _ in range(num)]
lst_index = 0
add = []
add_num = 1
log = []
check = True

while lst_index < num:
    if lst[lst_index] >= add_num:
        add.append(add_num)
        log.append('+')
        add_num += 1
    else:
        if lst[lst_index] == add[len(add)-1]:
            add.pop()
            log.append('-')
            lst_index += 1
        else:
            print('NO')
            check = False
            break

if check:
    print(*log,sep="\n")