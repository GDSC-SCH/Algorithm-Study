# 시간초과

c = []

def bble(c):
    for _ in range(len(c)):
        for i in range(len(c)-1):
            if c[i][0] > c[i+1][0]:
                c[i], c[i+1] = c[i+1], c[i]

for _ in range(int(input())):
	a,b = map(str,input().split())
	c.append([int(a),b])

bble(c)

for i in range(len(c)):
	print(c[i][0],c[i][1])