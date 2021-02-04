import sys

for _ in range(int(sys.stdin.readline())):
    a, *b = map(int,sys.stdin.readline().split())
    num = 0

    for i in b:
        if sum(b)/a < i:
            num += 1

    print("%0.3f%%" % (float(num/a)*100))