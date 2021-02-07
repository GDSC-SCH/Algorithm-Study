# 시간초과

llist = []

def make_one(n,cnt):
    if n == 1:
        llist.append(cnt)
        return
    if n < 1:
        return
    if n % 3 == 0:
        make_one(n//3,cnt+1)
    if n % 2 == 0:
        make_one(n//2,cnt+1)
    make_one(n-1,cnt+1)

n = int(input())
make_one(n,0)
print(min(llist))