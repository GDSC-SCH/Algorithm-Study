import sys

a = int(sys.stdin.readline())
b = a
cnt = 0

while 1:
    c = (b//10 + b%10) % 10
    b = c + (b % 10) * 10
    cnt += 1
    if a == b:
        break

print(cnt)