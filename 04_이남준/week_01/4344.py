test_case = int(input())

for i in range(test_case):
    stu_info = list(map(int, input().split()))

    number_of_stu = stu_info[0]
    stu_score_list = stu_info[1:]
    stu_score_avg = sum(stu_score_list) / number_of_stu

    avg_count = 0
    for j in stu_score_list:
        if j > stu_score_avg:
            avg_count = avg_count + 1

    result = avg_count/number_of_stu * 100
    print('%.3f' % round(result, 3) + '%')