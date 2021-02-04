def d(n):
    a=0
    for x in list(str(n)):
        a=a+int(x)
    return n+a

li=[]
for i in range(1,10001):
    li.append(d(i))

for j in range(1,10001):
    if j in li:
        pass
    else:
        print(j)