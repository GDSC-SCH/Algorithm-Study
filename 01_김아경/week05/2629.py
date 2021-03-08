N = int(input())
weight = [int(x) for x in input().split()]
M = int(input())
check = [int(x) for x in input().split()]

dp = [False]*(sum(weight)+1)
dp[0] = True

for w in weight:
    for i, e in enumerate(dp[:]):
        if e:
            if not(dp[i+w]):
                dp[i+w] = True

for w in weight:
    for i, e in enumerate(dp[:]):
        if e:
            if i-w >= 0:
                if not(dp[i-w]):
                    dp[i-w] = True
                    
for c in check:
    if c > len(dp)-1: # 구슬 무게가 추 무게보다 클때
        print('N', end = ' ')
    else:
        if dp[c]:
            print('Y', end = ' ')
        else:
            print('N', end = ' ')