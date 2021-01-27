user_input = int(input())
Box = 0
while True:
    if (user_input % 5) == 0:
        Box = Box + (user_input//5)
        print(Box)
        break
    user_input = user_input-3
    Box += 1
    if user_input < 0:
        print("-1")
        break