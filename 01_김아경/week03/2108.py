import sys

N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for i in range(N)]   
data_s = sorted(data)
    
print(round(sum(data)/N)) # average
print(data_s[N//2]) # median

# mode
from collections import Counter
data_c = Counter(data_s).most_common()

if len(data_c) > 1:
    if int(data_c[0][1]) == int(data_c[1][1]):
        print(data_c[1][0])
    else:
        print(data_c[0][0])
else:
    print(data[0])
    
# range
print(max(data) - min(data))