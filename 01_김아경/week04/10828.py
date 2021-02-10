import sys

stack = []

N = int(sys.stdin.readline())

for _ in range(N):
    inp = sys.stdin.readline().split()
    if inp[0] == 'push':
        stack.append(int(inp[1]))
    elif inp[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif inp[0] == 'size':
        print(len(stack))
    elif inp[0] == 'empty':
        print(0 if stack else 1)
    elif inp[0] == 'top':
        print(stack[-1] if stack else -1)