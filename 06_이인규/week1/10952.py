import sys

while 1:
    a,b = map(int,sys.stdin.readline().split())
    if ( a and b ) == 0:
        break
    print(a+b)