import sys
input=sys.stdin.readline

i=0
li=[]
while i<9:
    n=int(input())
    li.append(n)
    i+=1
print(max(li))
print(int(li.index(max(li)))+1)