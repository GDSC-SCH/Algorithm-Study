a = int(input())
answer = -1

for x in range((a+5)//5,-1,-1):

    y = (a-5*x)/3

    if y >= 0 and y%1 == 0.0:
        answer = x + y
        break

print(int(answer))