a, b = map(str, input().split())

rev_a = a[::-1]
rev_b = b[::-1]

if rev_a > rev_b:
    print(rev_a)
else:
    print(rev_b)
