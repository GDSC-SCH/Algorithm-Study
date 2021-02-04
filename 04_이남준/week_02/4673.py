none_self_number_list = [] # 생성자가 있는 숫자
self_number_list = [] # 생성자가 없는 숫자

number = 1
while True:
    d_n = number
    for i in str(number):
        d_n += int(i)
    
    if number > 10000:
        break

    if d_n not in none_self_number_list:
        none_self_number_list.append(d_n)

    number += 1

none_self_number_list.sort()

i = 1
while True:
    if i > 10000:
        break

    if i not in none_self_number_list:
        self_number_list.append(i)
        print(i)

    i += 1