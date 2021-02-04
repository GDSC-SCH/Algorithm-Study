user_input = input().upper()
keyWord = list(set(user_input))

freq = []
for i in keyWord:
    cnt = user_input.count(i)
    freq.append(cnt)

if freq.count(max(freq)) > 1: 
    print('?')
else:
    print(keyWord[freq.index(max(freq))])
