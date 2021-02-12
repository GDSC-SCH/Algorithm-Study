import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

P = {}
for index, value in enumerate(p):
    P[index+1] = value # dict에 저장(key: 사람 번호, value: 인출 시간)

P = sorted(P.items(), key=lambda x: x[1]) # 인출 시간을 기준으로 오름차순 정렬

result = 0
for i in range(len(P)): # 정렬된 목록을 순회
    time = 0
    for j in range(i+1): # 해당 사람까지의 대기시간 + 인출시간을 계산
        time += P[j][1]
    result += time # 총 시간에 더해줌

print(result)