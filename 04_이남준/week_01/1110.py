def str_sum(number: str) -> str:
    result = int(number[0]) + int(number[-1])
    return str(result)

number = input()

init_number = number
count = 0

if 0 <= int(number) < 10:
    number = '0' + number

while True:
    first_step = str_sum(number)
    result_number = number[-1] + first_step[-1]

    count = count + 1

    if int(result_number) == int(init_number):
        break

    number = result_number

print(count)