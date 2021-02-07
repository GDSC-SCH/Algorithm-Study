# N, K 값 입력받기
N, K = map(int, input().split())

coin = []
count=0

# 리스트에 값 추가
for i in range(N):
    c = int(input())
    coin.append(c)

for i in range(1, N+1):
    div_coin = coin[-i]
    if K>-div_coin:
        div_up = K//div_coin
        K -= div_coin*div_up
        count+=div_up

print(count)
