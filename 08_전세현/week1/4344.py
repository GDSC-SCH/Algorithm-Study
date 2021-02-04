import sys
input=sys.stdin.readline

n=int(input())
result=[]
for i in range(0,n):
    li=list(map(int,input().split()))
    avg=sum(li[1:])/li[0]
    cnt=0
    for j in li[1:]:
        if j > avg:
            cnt+=1
    a=cnt/li[0]*100
    print("%.3f" %round(a,3)+"%")

