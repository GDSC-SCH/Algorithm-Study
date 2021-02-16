# 메모리초과...

def check(sum,num):
    if num == -1:
        chk.append(sum)
        return
    check(sum + lst1[num],num-1)
    check(sum - lst1[num],num-1)

lst1_num = int(input())
lst1 = list(map(int,input().split()))
int(input())
lst2 = list(map(int,input().split()))
chk = []

check(0,lst1_num-1)

for i in lst2:
    if i in chk:
        print("Y",end=" ")
    else:
        print("N",end=" ")