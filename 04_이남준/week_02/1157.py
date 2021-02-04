word = input()

many_char = {}
for i in word:
    i = i.upper()
    if i in many_char.keys():
        many_char[i] += 1
    else:
        many_char[i] = 1

many_char = sorted(many_char.items(), reverse=True, key=lambda x: x[1])

if len(word) == 1:
    print(many_char[0][0])
else:
    if many_char[0][1] == many_char[1][1]:
        print('?')
    else:
        print(many_char[0][0])