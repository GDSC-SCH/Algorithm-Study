n_weight = int(input())
weights = [int(x) for x in input().split()]
n_ball = int(input())
balls = [int(x) for x in input().split()]

def scale(now, left, right):
    """
    추를 왼쪽, 오른쪽, 안 올리는 것 세가지 모두를 시도함
    :param now: 이번에 확인할 추의 index
    :param left: 왼쪽의 무게
    :param right: 오른쪽의 무게
    :param possible: 가능한 경우들
    :return:
    """
    new = abs(left - right)
    if new not in possible:
        possible.append(new)
    if now == n_weight:
        return
    if answer[now][new] == 0:
        # answer[i][j] : i번째 추, j무게
        # 다른 scale 함수 과정 중에서 j 무게에 대해 계산했으면 넘어감
        scale(now + 1, left + weights[now], right)
        scale(now + 1, left, right + weights[now])
        scale(now + 1, left, right)
        answer[now][new] = 1

possible = []
maximum = sum(weights)
answer = [[0] * maximum for _ in range(n_weight+1)]

scale(0, 0, 0)
for i in range(n_ball):
    if balls[i] in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')