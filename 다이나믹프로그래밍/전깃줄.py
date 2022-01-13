import bisect
import sys
input = sys.stdin.readline

k = int(input())

graph = []

for _ in range(k):
    start, end = map(int,input().split())
    graph.append([start, end])

graph.sort(key= lambda x: x[0])

dp = [graph[0][1]]
for i in range(len(graph)):
    if graph[i][1] > dp[-1]:
        dp.append(graph[i][1])
    else:
        idx = bisect.bisect_left(dp, graph[i][1])
        dp[idx] = graph[i][1]

print(len(graph) - len(dp))


    

# print(result)