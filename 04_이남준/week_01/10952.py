# 입력을 한 번에 받고 출력을 한 번에 하는 것인지 헷갈렸으나
# 출력 조건은 '각 테스트 케이스마다 A+B를 출력한다' 이므로 매번 출력으로 생각함

while(True):
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    print(A + B)