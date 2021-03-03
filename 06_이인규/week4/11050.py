def factory(num,result):
    if num <= 1:
        return result
    
    return factory(num-1,result*num)
    

n, k = map(int,input().split())

up = factory(n,1)
down1 = factory(n-k,1)
down2 = factory(k,1)

print(int(up/(down1*down2)))