# 미완

def all(sum,ind,plus,unplus,undiv,div,a):
    if plus+unplus+undiv+div == a-1:
        result.append([sum])
        return
    all(sum+llist[ind],ind,plus+1,unplus,undiv,div,a)
    all(sum-llist[ind],ind,plus,unplus+1,undiv,div,a)
    all(sum*llist[ind],ind,plus,unplus,undiv+1,div,a)
    all(sum/llist[ind],ind,plus,unplus,undiv,div+1,a)

llist = []
result = []

a = int(input())
llist = list(map(int,input().split()))
