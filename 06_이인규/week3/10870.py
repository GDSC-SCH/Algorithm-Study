fibo = [0,1]

a = int(input())

if a == 0:
    print(0)
elif a == 1:
    print(1)
else:
    for i in range(a-1):
        fibo.append(fibo[i]+fibo[i+1])

    print(fibo[len(fibo)-1])