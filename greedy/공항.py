import sys

def GetParent(parent, a):
    if(parent[a] == a): 
        return a
    else:
        parent[a] = GetParent(parent, parent[a])
        return parent[a]

def UnionNode(parent, a , b):
    parentA = GetParent(parent,a)
    parentB = GetParent(parent,b)
    if(parentA > parentB) : parent[a] = parentB
    else: parent[b] = parentA


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
parent = {i : i for i in range(G+1)}

items = []
for i in range(P):
    items.append(int(sys.stdin.readline()))

cnt = 0

for item in items:
    j = GetParent(parent, item)
    if(j == 0): break        
    UnionNode(parent, j, j-1)
    cnt += 1

print(cnt)

