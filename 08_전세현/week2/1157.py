import sys

n=sys.stdin.readline().strip().upper()

new_n=list(set(n))

li=[]
for x in new_n:
    count=n.count(x)
    li.append(count)

if not li.count(max(li)) == 1:
    print('?')
else:
    max_num=li.index(max(li))
    print(new_n[max_num])