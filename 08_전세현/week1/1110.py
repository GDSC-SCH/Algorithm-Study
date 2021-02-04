import sys
input=sys.stdin.readline

n=int(input())
a=n
cnt=0
while True:
    tmp=(n//10)+(n%10)
    n2=((n%10)*10)+tmp%10
    cnt+=1
    n=n2
    if n2==a:
        break
print(cnt)