a = int(input())

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0

while 1:
    call = 1000000*one + 100000*two + 10000*three + 1000*four + 100*five + 10*six + seven
    answer = call + one + two + three + four + five + six + seven
    
    if call == a-1:
        print(0)
        break

    if answer == a:
        print(call)
        break

    seven += 1

    if seven == 10:
        seven = 0
        six += 1
    if six == 10:
        six = 0
        five += 1
    if five == 10:
        five = 0
        four += 1
    if four == 10:
        four = 0
        three += 1
    if three == 10:
        three = 0
        two += 1
    if two == 10:
        two = 0
        one += 1