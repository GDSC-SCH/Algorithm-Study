# 시간초과

input()
N_list = list(map(int,input().split()))
input()
M_list = list(map(int,input().split()))

M_list.sort()

N_index = 0
M_index = 0

while N_index != (len(N_list)):
    if N_list[N_index] == M_list[M_index]:
        print(1)
        N_index += 1
    elif N_list[N_index] > M_list[M_index]:
        M_index += 1
    else:
        print(0)
        M_index += 1