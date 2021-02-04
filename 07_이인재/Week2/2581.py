start = int(input())
last = int(input())
ans = []
for num in range(start, last+1):
    err = 0
    if num > 1 :
        for i in range(2, num):  
            if num % i == 0:
                error += 1
                break  
        if err == 0:
            ans.append(num) 
            
if len(ans) > 0 :
    print(sum(ans))
    print(min(ans))
else:
    print(-1)