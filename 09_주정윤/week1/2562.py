num =9
list=[]

for i in range(num):
    a = int(input())
    list.append(a)
    
print(max(list))


print(list.index(max(list))+1)

