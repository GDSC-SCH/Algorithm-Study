a = int(input())
b = 2

while a != 1:
    if a % b == 0:
        print(b)
        a = a // b
        b = 2
    else:
        b += 1