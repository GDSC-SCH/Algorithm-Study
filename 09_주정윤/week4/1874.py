n = int(input())

print_list=[]
count=0
s=[]
msg=True

for i in range(0, n):
    a = int(input())
    
    while count<a: #push
        count+=1 
        s.append(count)
        print_list.append("+")
    
    if s[-1]==a: #pop
        s.pop()
        print_list.append("-")
    else:
        msg=False
        break



if msg==False:
    print("NO")
else:
    for i in range(len(print_list)):
        print(print_list[i])