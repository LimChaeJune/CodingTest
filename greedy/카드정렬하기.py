import heapq
import sys

C = int(sys.stdin.readline())


newlist = []
for i in range(C):
   newlist.append(int(sys.stdin.readline()))

heapq.heapify(newlist)

if(len(newlist) == 1):
    print(0)
else:
    result = 0
    while(len(newlist) > 1):
        first = heapq.heappop(newlist)
        second = heapq.heappop(newlist)
        sum = first + second
        result += sum
        heapq.heappush(newlist, sum)

    print(result)

