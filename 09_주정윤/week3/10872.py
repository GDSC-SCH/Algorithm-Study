a = int(input())

sum=1
real_a = a
while True:
    if a==0:
        break
    sum=sum*a
    a=a-1

print(sum)