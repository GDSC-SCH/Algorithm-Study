N = int(input())

n5 = N // 5
is_ok = False
while n5 >= 0:
    if (N - n5 * 5) % 3 == 0:
        print(n5 + (N - n5 * 5) // 3)
        is_ok = True
        break
    n5 -= 1
if not is_ok:
    print(-1)