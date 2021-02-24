a,b = map(int,input().split())
lst = []
cnt = 0

for _ in range(a):
    lst.append(int(input()))

lst.reverse()

for i in lst:
    cnt += b//i
    b = b%i

print(cnt)