import sys
input=sys.stdin.readline

a,b=map(int,input().split())

a=str(a)
b=str(b)
n_a=int(a[::-1])
n_b=int(b[::-1])
print(max(n_a,n_b))