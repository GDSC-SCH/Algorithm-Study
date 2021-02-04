import sys

N = int(sys.stdin.readline())

people_list = []
for i in range(N):
    people = sys.stdin.readline().split()
    people.insert(0, i)
    people[1] = int(people[1])
    people_list.append(people)

people_list = sorted(people_list, key=lambda x: (x[1], x[0]))

for i in people_list:
    print(i[1], i[2])