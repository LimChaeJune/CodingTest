from itertools import combinations
N, M = map(int,input().split())


stores = []
homes = []
for i in range(N):
  row =  list(map(int, input().split()))
  for j in range(len(row)):
    if row[j] == 1:
      homes.append((i,j))
    elif row[j] == 2:
      stores.append((i,j))

storeM = combinations(stores, M)
answer = 99999
for combiStore in storeM:
  homeVis = [99999] * len(homes)
  for combi in combiStore:
    for j in range(len(homes)):
      chicRan = abs(combi[0]-homes[j][0])+abs(combi[1]-homes[j][1])
      homeVis[j] = min(homeVis[j], chicRan)
      
  answer = min(sum(homeVis), answer)
  
print(answer)