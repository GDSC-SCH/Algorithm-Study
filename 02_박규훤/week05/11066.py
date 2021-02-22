import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    length = int(input())
    nums = tuple(int(x) for x in input().split())

    # table[i][j] : i ~ j 파일을 합치는 시간
    table = [[0] * length for _ in range(length)]
    for i in range(length-1):
        table[i][i+1] = nums[i] + nums[i+1]
        for j in range(i+2, length):
            table[i][j] = table[i][j-1] + nums[j]

    # gap : 간격
    # i ~ j 파일을 합치는 최소 시간은 [1](i ~ k 파일 합치는 시간) + [2](k+1 ~ j 파일 합치는 시간) +
    #                                                               [3](앞의 두 파일을 합치는 시간, 즉 i ~ j의 합)
    # 여러 개의 k 중에서 합치는 시간이 가장 작은 값을 찾으면 됨
    for gap in range(2, length):
        for i in range(length - gap):
            j = i+gap
            minimum = [table[i][k] + table[k+1][j] for k in range(i, j)]
            # table[i][j]는 [3]으로만 이루어져 있어서 [1] + [2]를 추가하는 것임
            table[i][j] += min(minimum)

    print(table[0][-1])
