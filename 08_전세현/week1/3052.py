import sys
input=sys.stdin.readline

count=0
i=0
li=[]

while i<10:
    n=int(input())
    li.append(n%42)    
    i+=1

li=set(li)
print(len(li))