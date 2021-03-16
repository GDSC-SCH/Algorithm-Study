import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    order = sys.stdin.readline()
    if order[:2] == "pu": # push
        o, v = order.split()
        stack.append(int(v))
    elif order[:2] == "po": # pop
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[:2] == "si": # size
        print(len(stack))
    elif order[:2] == "em": # empty
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[:2] == "to": #top
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])