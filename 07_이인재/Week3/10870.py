user_input = int(input())

def fi(n):
    if n<=1:
        return n
    return fi(n-1) + fi(n-2)

if user_input == 0:
    print(0)
else:
    print(fi(user_input))

