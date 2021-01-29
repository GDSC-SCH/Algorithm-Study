user_input = int(input())

p1 = 1
p2 = 2
p3 = 3

def Hanoi(n, p1, p2, p3):
    if n == 1:    
        print(p1, p3)
    else:
        Hanoi(n-1,p1, p3, p2)
        print(p1, p3)
        Hanoi(n-1,p2,p1,p3)
cnt = 1
for i in range(user_input -1):
    cnt = cnt*2+1
print(cnt)
Hanoi(user_input, p1, p2, p3)