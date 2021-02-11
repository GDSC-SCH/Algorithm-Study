# 시간초과

N, M = map(int,input().split())
N_list = list(map(int,input().split()))
for i in range(max(N_list),-1,-1):
    sum = 0
    for j in N_list:
        if i < j:
            sum += j - i
    if sum >= M:
        print(i)
        break