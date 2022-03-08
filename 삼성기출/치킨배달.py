
import bisect


N,M = map(int, input().split())

graph = []
stores = []
homes = []
for i in range(N):
  row = list(map(int, input().split()))
  for j in range(N):
    graph.append(row[j])
    if row[j] == 2: 
      stores.append([i,j])
    elif row[j] == 1:
      homes.append([i,j])

storesVal = [0] * len(stores)
homeVis = [99999] * len(homes)
for i in range(len(stores)):  
  for j in range(len(homes)):
    x = (homes[j][0]+1) - (stores[i][0]+1)
    y = (homes[j][1]+1) - (stores[i][1]+1)
    chicRange =  (abs(x) + abs(y))
    homeVis[j] = min(homeVis[j], chicRange)
    if chicRange == homeVis[j]:
        storesVal[i] += chicRange

while len(stores) > M:
    maxVal = max(storesVal)
    idx = storesVal.index(maxVal)
    storesVal.pop(idx)
    stores.pop(idx)

homeVis = [99999] * len(homes)
for i in range(len(stores)):  
  for j in range(len(homes)):
    x = (homes[j][0]+1) - (stores[i][0]+1)
    y = (homes[j][1]+1) - (stores[i][1]+1)
    chicRange =  (abs(x) + abs(y))
    homeVis[j] = min(homeVis[j], chicRange)    

print(sum(homeVis))