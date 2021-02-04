import sys
input=sys.stdin.readline

x,y,w,h=map(int,input().split())

if w>1 and h <=1000:
    if 1<=x<=w-1 and 1<=y<=h-1:
        print(min([x,y,w-x,h-y]))