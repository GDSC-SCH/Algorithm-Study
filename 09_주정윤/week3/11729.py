
MSG_FORMAT="{} {}"

def move(num, start, to):
    print(MSG_FORMAT.format(start, to))

def hanoi(num, start, to, via):
    if num==1:
        move(1, start, to)
    else:
        hanoi(num-1, start, via, to)
        move(num, start, to)
        hanoi(num-1, via, to, start)


a = int(input())

count=1
for i in range(a-1):
    count=count*2+1

print(count)
hanoi(a, '1', '3', '2')
