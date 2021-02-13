import sys

T = int(sys.stdin.readline())
site = []
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    site.append((N, M))

fac = {0: 1} # 0! = 1 저장
''' 팩토리얼을 계산해 저장하는 부분 '''
for i in site:
    result = 1
    for j in range(1, i[1] + 1):
        result *= j
        if j not in fac.keys():
            fac[j] = result

# 팩토리얼 값 return 함수
def get_facto(num: int) -> int:
    global fac
    return fac[num]

# nCk 계산
for i in site:
    print( get_facto(i[1]) // ( get_facto(i[0]) * get_facto(i[1] - i[0]) ) )