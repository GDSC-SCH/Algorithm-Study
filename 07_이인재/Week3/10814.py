user_input = int(input())

arr = []

for i in range(user_input):
    age, name = input().split(" ")
    arr.append((int(age),  name))
arr.sort(key= lambda age:(age[0]))

for j in arr:
    print(j[0], j[1])