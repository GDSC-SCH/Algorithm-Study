H, M = map(int, input().split())

if H == 0:
    if M-45 < 0:
        print(23, 60+M-45)
    else:
        print(0, M-45)
else:
    if M-45 < 0:
        print(H-1, 60+M-45)
    else:
        print(H, M-45)
        
#%%
H, M = map(int, input().split())

if M-45 < 0:
    H -= 1
    M = 60 + M - 45
    if H < 0:
        H = 23
    print(H, M)
else:
    M = M - 45
    print(H, M)