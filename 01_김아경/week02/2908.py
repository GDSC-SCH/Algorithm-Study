a, b = map(int, input().split())

a = a - (a//100*100 + a%10) + (a%10*100 + a//100)
b = b - (b//100*100 + b%10) + (b%10*100 + b//100)

if a < b:
    print(b)
else:
    print(a)