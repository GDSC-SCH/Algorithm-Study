T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    people = [i+1 for i in range(n)]
    
    for i in range(k):
        for j in range(n-1):
            people[j+1] = people[j] + people[j+1]
    
    print(max(people))