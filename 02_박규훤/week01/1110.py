original = int(input())
N = original
count = 0

while count == 0 or N != original:
    s = sum([int(i) for i in str(N)])
    N = int(N%10*10 + s%10)
    count += 1

print(count)