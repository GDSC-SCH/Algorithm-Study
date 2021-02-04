import sys
input=sys.stdin.readline

M=int(input())
N=int(input())
li=[]
for i in range(M,N):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
            if cnt >2:
                break
    if cnt == 2:
        li.append(i)

if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))