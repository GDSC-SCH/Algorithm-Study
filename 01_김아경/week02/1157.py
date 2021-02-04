text = [x.upper() for x in input()]
from collections import Counter
counter = Counter(text)

output = [key for key, value in counter.items() if value == max(counter.values())]

if len(output) == 1:
    print(output[0])
else:
    print('?')