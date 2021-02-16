import sys

a = int(sys.stdin.readline())

for i in range(1,a+1):
    print(' '*(a-i)+'*'*i) # 각자의 개수만 출력