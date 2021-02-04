A = int(input())
B = input()

B_list = [int(i) * A for i in reversed(B)]
ret = 0
multi = 1
for b in B_list:
    print(b)
    ret += multi * b
    multi *= 10
print(ret)