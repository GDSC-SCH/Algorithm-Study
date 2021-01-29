n = int(input())
a = 0
b = 1
fibonacci = 0

if n != 1:
    for i in range(n-1):
        fibonacci = a + b
        a = b
        b = fibonacci
        
    print(fibonacci)
else:
    print(1) 