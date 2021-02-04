ans = int(input())
ans_2 = ans
count=0

while True:
    front = ans_2//10
    back = ans_2%10   
    sum = (front+back)%10

    ans_2 = back*10+sum 
    count+=1
    if ans==ans_2:
        break

print(count)
