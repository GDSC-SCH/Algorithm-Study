import sys
input=sys.stdin.readline

a=int(input())
b=int(input())

print(a*(b%10))
print(round(a*((b%100)-(b%10))/10))
print(a*(int(b/100)))
print(a*b)