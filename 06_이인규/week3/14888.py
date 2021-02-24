import sys

lst = []
res = []

def calculator(num_index,result,p,m,q,d):

    if p+m+d+q == 0:
        res.append(result)
        return

    if p > 0:
        calculator(num_index+1,result+lst[num_index],p-1,m,q,d)
    if m > 0:
        calculator(num_index+1,result-lst[num_index],p,m-1,q,d)
    if q > 0:
        calculator(num_index+1,result*lst[num_index],p,m,q-1,d)
    if d > 0:
        if result < 0:
            result = abs(result)//lst[num_index]
            calculator(num_index+1,-result,p,m,q,d-1)
        else:
            calculator(num_index+1,result//lst[num_index],p,m,q,d-1)

int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
p, m, q, d = map(int,sys.stdin.readline().split())

calculator(1,lst[0],p,m,q,d)

print(max(res))
print(min(res))