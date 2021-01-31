N = int(input())

result = 0
have_value = False
for num in range(1, N):
    result += num
    for i in str(num):
        result += int(i)

    if result == N:
        have_value = True
        print(num)
        break
    result = 0

if have_value == False:
    print(0)