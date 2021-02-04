number_list = []

for i in range(9):
    number = int(input())
    number_list.append(number)

max_num = max(number_list)
for i, value in enumerate(number_list):
    if value == max_num:
        print(value)
        print(i+1)