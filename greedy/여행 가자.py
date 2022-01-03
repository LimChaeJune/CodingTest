import sys
input = sys.stdin.readline

def GetParent(parent, a):
    if parent[a] == a:
        return a             

    parent[a] = GetParent(parent, parent[a])
    return parent[a]

def UnionNode(parent, a , b):
    a = GetParent(parent,a)
    b = GetParent(parent,b)
    if(a < b) : 
        parent[b] = a
    elif (a < b): 
        parent[a] = b
    else:
        return

e = int(input())
c = int(input())

parent = {i : i for i in range(e+1)}

for i in range(1, e + 1):
    info = list(map(int, input().split()))

    for j in range(1, len(info) + 1):
        if info[j-1] == 1:
            UnionNode(parent, i, j)

plans = list(map(int, input().split()))
result = []

result = set([GetParent(parent, i) for i in plans])
if len(result) != 1:
    print('NO')
else:
    print('YES') 