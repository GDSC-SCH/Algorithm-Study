import sys

# 10개의 값을 입력받아서 42로 나눈 나머지를 리스트에 저장한다.
# 이때 set함수에 의해서 중복값이 제거된 리스트만 출력된다.
print(len(set([int(sys.stdin.readline())%42 for _ in range(10)])))