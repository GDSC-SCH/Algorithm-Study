def check_weight(max_num, index_number, left, right):
    if max_num == index_number:
        return 0

lst = []
max_num = int(input())
ball_list = list(map(int,input().split()))
int(input())
check_list = list(map(int,input().split()))
check_weight(max_num,0 , 0, 0)

for i in check_list:
    if i in lst:
        print('Y',end=' ')
    else:
        print('N',end=' ')

print(lst)