number_list = []

for i in range(10):
    number = int(input())
    number_list.append(number)

remainder_list = []

for i in number_list:
    if i % 42 not in remainder_list:
        remainder_list.append(i % 42)

print(len(remainder_list))