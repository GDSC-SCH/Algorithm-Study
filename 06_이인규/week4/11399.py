num = int(input())

a = list(map(int,input().split()))

a.sort()
result = 0

for i in range(num+1):
	result += sum(a[:i])
	
print(result)