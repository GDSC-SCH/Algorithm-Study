def find(n):
    real_n = n
    for i in list(str(n)):
        real_n = real_n+int(i)
    return real_n

remove_list=[]
for i in range(1, 10000):
    a = find(i)
    remove_list.append(a)

for i in range(1, 10000):
    if i in remove_list:
        pass
    else:
        print(i)

