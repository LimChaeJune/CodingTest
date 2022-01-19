H , W = map(int,input().split()) 

walls = list(map(int,input().split()))


result = 0
rains = []

maxVal = 0
maxIdx = 0

for i in range(len(walls)):
    if maxVal < walls[i]:
        maxVal = walls[i]
        maxIdx = i

temp = 0
for j in range(maxIdx + 1):
    if walls[j] > temp:
        temp = walls[j]
    result += temp

temp = 0
for j in range(len(walls)-1, maxIdx, -1):
    if walls[j] > temp:
        temp = walls[j]
    result += temp


    
print(result - sum(walls))
    


