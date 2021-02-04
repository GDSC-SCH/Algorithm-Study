N = int(input())
n = N
count = 0

while count == 0 or n != N: #F or T = T
    count += 1
    
    if n < 10:
        n = n*10 + n
    else:
        n = n%10*10 + (n//10 + n%10)%10
    
    

print(count)