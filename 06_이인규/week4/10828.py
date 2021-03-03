import sys

def push(command):
    global length
    lst.append(command)
    length += 1

def pop():
    global length
    if length == 0:
        print(-1)
    else:
        print(lst[length-1])
        lst.pop()
        length -= 1

def empty():
    global length
    if length == 0:
        print(1)
    else:
        print(0)

def top():
    global length
    if length == 0:
        print(-1)
    else:
        print(lst[length-1])

lst = []
length = 0

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        push(command[1])
    
    elif command[0] == 'pop':
        pop()
    
    elif command[0] == 'size':
        print(length)
    
    elif command[0] == 'empty':
        empty()

    elif command[0] == 'top':
        top()