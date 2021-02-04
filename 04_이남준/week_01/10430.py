numbers = input()
A, B, C = map(int, numbers.split())

''' 이전 코드
numbers_list = numbers.split()

A = int(numbers_list[0])
B = int(numbers_list[1])
C = int(numbers_list[2])

비효율적이고 노가다(?)삘
'''

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)