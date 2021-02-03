a = int(input())
b = a
step = a//3+1
step2 = a//2+1
c = []

for i in range(step,0,-1):
    for j in range(step2,0,-1):
        print("check",3*i*2*j)
        if (3*i)*(2*j) + 1 == b:
            c.append(i+j+1)
        if (3*i)*(2*j) == b:
            c.append(i+j)

print(c)
