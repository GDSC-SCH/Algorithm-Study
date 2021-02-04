user_input = int(input())
i = 2
while user_input != 0:
    if user_input %i == 0:
        user_input = user_input/i
        print(int(user_input))
    else:
        i +=1