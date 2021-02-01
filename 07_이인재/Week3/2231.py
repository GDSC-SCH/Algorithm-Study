user_input = int(input())

for i in range(1, user_input+1):
    tmp = list(map(int, str(i)))
    result = i+ sum(tmp)

    if result == user_input:
        print(i)
        break;

    elif i == user_input:
        print(0)
