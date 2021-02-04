N = int(input())

if N%5 == 0:
    print(N//5)

elif N%5 == 1:
    print((N-(3*2))//5 + 2)
    
elif N%5 == 2 and N-12 >= 0: #7
    print((N-(3*4))//5 + 4)

elif N%5 == 3: 
    print((N-3*1)//5 + 1)

elif N%5 == 4 and N-9 >= 0: #4
    print((N-(3*3))//5 + 3)

else:
    print(-1)