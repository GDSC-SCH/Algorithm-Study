num = int(input())
 
i = 2
while num != i:
    while num%i == 0:
        print(i)
        num = int(num/i)
    if num == 1:
        break
    i+=1
if num != 1:
    print(int(num))
