""" ex)
3층 1  5  15 35
2층 1  4  10 20
1층 1  3  6  10
0층 1  2  3  4
"""
# 출력결과는 정상이나, 백준에서는 시간초과

apart = {0: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14}}


def how_many_lived(floor, ho):
    people = 0
    if floor == 0:
        return apart[0][ho]
    else:
        if apart.get(floor) != None:
            if apart[floor].get(ho) != None:
                return apart[floor][ho]
        for i in range(1, ho + 1):
            people += how_many_lived(floor - 1, i)
            apart[floor] = {ho: people}
        return people


test_case = int(input())

for case in range(test_case):
    floor = int(input())
    ho = int(input())

    if ho == 1:
        print(1)
    else:
        print(how_many_lived(floor, ho))
