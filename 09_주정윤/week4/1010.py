def gob(n):
    sum=1
    for i in range(1, n+1):
        sum = sum * i
    return sum


T = int(input())

N_list=[]
M_list=[]

for i in range(T):
    N, M = map(int, input().split())
    N_list.append(N)
    M_list.append(M)

for i in range(T):
    print(int(gob(M_list[i])/(gob(N_list[i])*gob(M_list[i]-N_list[i]))))
