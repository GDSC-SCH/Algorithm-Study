def three(a,c):
	for i in range(len(c)-1,-1,-1):
		if c[i] >= a:
			c[i-1] += c[i] // a
			c[i] = (c[i] % a) + 1
	print(*c,sep=' ')

def forr(a,c):
	c[len(c)-1] += 1
	three(a+1,c)

a,b = map(int,input().split())
c = []

for i in range(b-1):
	c.append(1)
c.append(0)
for _ in range(a**b):
	forr(a,c)