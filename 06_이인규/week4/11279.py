# 시간초과

array = []; enter = []

for _ in range(int(input())):
    enter.append(int(input()))

for i in enter:
    if i + len(array) == 0:
        print(0)
    elif i == 0:
        a = max(array)
        print(a)
        array.remove(a)
    else:
        array.append(i)