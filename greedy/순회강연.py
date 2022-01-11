import sys
import heapq
input = sys.stdin.readline

def heapsort(interable):
    h = []    

    for value in interable:
        heapq.heappush(h , value[1])
    
        if len(h) > value[0]:
             heapq.heappop(h)
    
    return h

n = int(input())

interable = []
for i in range(n):
    p, d = map(int,input().split())
    interable.append((d,p))

interable.sort(key = lambda x : (x[0]))

result = []
for item in interable:
    heapq.heappush(result, item[1])
    if len(result) > item[0]:
        heapq.heappop(result)

print(sum(result))

