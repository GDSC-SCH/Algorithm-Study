# 시간초과

input()
N_list = list(map(int,input().split()))
input()
M_list = list(map(int,input().split()))

for i in M_list:
    if i in N_list:
        print(1)
    else:
        print(0)