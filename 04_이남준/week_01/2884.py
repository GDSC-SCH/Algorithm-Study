hour, min = map(int, input().split())

if 45 <= min:
    min = min - 45
else:
    min = 60 - (45 - min)
    if hour == 0:
        hour = 23
    else:
        hour = hour - 1

print(hour, min)