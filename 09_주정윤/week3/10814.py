n = int(input()) 
list = [] 

for i in range(n): 
    age,name = input().split() 
    age = int(age) 
    list.append([age, name]) 
    
list.sort(key=lambda x: x[0]) 
    
for i in list: 
    print(*i)

