import heapq
import sys
input = sys.stdin.readline

N = int(input())

schedule =[]

for i in range(N):
  st, fns = map(int,input().split()) 
  schedule.append([st,fns])

schedule.sort()

result = []
heapq.heappush(result, schedule[0][1])
answer = 1

for i in range(1, N): 
    sche = schedule[i]
  
    if sche[0] < result[0]:        
      heapq.heappush(result, sche[1])
    else:
      heapq.heappop(result)
      heapq.heappush(result, sche[1])

print(len(result))

  