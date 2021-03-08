import sys

lst1 = []
lst2 = []

def check(i):
    return int(i in lst1)

sys.stdin.readline()
lst1 = set(list(map(int,sys.stdin.readline().split())))
sys.stdin.readline()
lst2 = list(map(int,sys.stdin.readline().split()))

for i in lst2:
    print(check(i))