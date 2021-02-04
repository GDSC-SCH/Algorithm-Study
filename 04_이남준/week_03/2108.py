import sys

def avg(n: int, num_list: list) -> float:
    result = 0
    for i in num_list:
        result += i
    return round(result/n)

def center(num_list: list) -> int:
    return num_list[len(num_list)//2]

def bindo(num_list: list) -> int:
    result = {}
    for i in num_list:
        if i not in result.keys():
            result[i] = 1
        else:
            result[i] += 1
    result = sorted(result.items(), reverse=True, key=lambda item: item[1])
    if len(result) == 1:
        return result[0][0]
    if result[0][1] == result[1][1]:
        return result[1][0]
    else:
        return result[0][0]

def distance(num_list: list) -> int:
    return num_list[-1] - num_list[0]

N = int(sys.stdin.readline())

num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

print(avg(N, num_list))
print(center(num_list))
print(bindo(num_list))
print(distance(num_list))