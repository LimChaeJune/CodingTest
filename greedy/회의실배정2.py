import heapq

N = int(input())
meets = []

for i in range(N):
  S, F = map(int, input().split())
  meets.append([S,F])

meets.sort()

rooms = []
print(meets)
heapq.heappush(rooms,meets[0])
for i in range(1, len(meets)):    
  if meets[i][0] < meets[i-0][1]:
    heapq.heappush(rooms, meets[i])
  else:    
    heapq.heappop(rooms)
    heapq.heappush(rooms, meets[i])

print(len(rooms))
  
  