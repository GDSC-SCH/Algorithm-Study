import sys

a = int(sys.stdin.readline()) # 입력
b = a # 변화되는 값이 원래 값과 비교될때 사용
cnt = 0 # 횟수 카운트

while 1:
    c = (b//10 + b%10) % 10
    b = c + (b % 10) * 10
    cnt += 1
    if a == b:
        break

print(cnt)