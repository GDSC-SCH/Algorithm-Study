a, b = [int(input()) for _ in range(2)]

x = a*(b%10)
y = a*(b//10%10)
z = a*(b//100%10)

print(x, y, z, x+y*10+z*100, sep = '\n')