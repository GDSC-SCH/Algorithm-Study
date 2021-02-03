N = int(input()) #21

for i in range(1, N+1):
    decom = [int(str(i)[j]) for j in range(len(str(i)))]

    if N == (i + sum(decom)):
        print(i)
        break
    
    if N == i:
        print(0)