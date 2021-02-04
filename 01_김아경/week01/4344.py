C = int(input())
for i in range(C):
    num = [int(i) for i in input().split()]
    n = num[0]
    aver = (sum(num) - n)/n
    
    #total = 0
    #for j in range(1, n+1):
    #    if num[j] > aver:
    #        total += 1
    
    total = [1 for j in range(1, n+1) if num[j] > aver]
    
    print('%.3f' % (sum(total)/n * 100), '%', sep = '')