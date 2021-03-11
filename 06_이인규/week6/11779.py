# 보류

x = int(input())
y = int(input())

lst = [[0 for _ in range(x)] for __ in range(x)]

for _ in range(y):
    a,b,c = map(int,input().split())

    lst[a-1][b-1] = c

start, end = map(int,input().split())

short = lst[0][end-1]

for i in range(1,x):
    if short > lst[i][end-1]:
        short = lst[i][end-1]