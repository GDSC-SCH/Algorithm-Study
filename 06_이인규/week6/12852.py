import sys

num = int(sys.stdin.readline())

lst = [0,1,1]
log = '1'

for i in range(4,num+1):
    lst.append(0)

    lst[i-1] = lst[i-2] + 1
    gd = i

    if i % 3 == 0 and lst[i-1] > lst[i//3-1] + 1:
        gd = i//3
        lst[i-1] = lst[i//3-1] + 1
    
    if i % 2 == 0 and lst[i-1] > lst[i//2-1] + 1:
        gd = i//2
        lst[i-1] = lst[i//2-1] + 1

    log += ' ' + str(gd)

print(lst[num-1])
print(log[:-1])