user_input = int(input())

for b in range(user_input):
    k = int(input())
    n = int(input())

    people = [ i for i in range(1, n+1)]
    for q in range(k):

        for j in range(1,n):

            people[j] += people[j-1]

    print(people[-1])