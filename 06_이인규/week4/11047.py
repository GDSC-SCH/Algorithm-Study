# 시간초과

def money(n,cnt):
    for i in kinds:
        while 1:
            if n >= i:
                n -= i
                cnt += 1
            else:
                break
    return cnt

a,b = map(int,input().split())
kinds = []

for _ in range(a):
    kinds.append(int(input()))

kinds.reverse()

print(money(b,0))