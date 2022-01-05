from collections import deque
from collections import defaultdict

N, M = map(int,input().split())

graph = defaultdict(list)

def bfs(graph, start):
    visited = {}    
    queue = deque()
    queue.append((start, 0))
    visited[start] = 0

    while(queue):        
        x, cnt = queue.popleft()                     

        if len(visited) == N : 
            break

        for f in graph[x]:                        
            if f in visited:
                continue

            queue.append((f, cnt +1))
            visited[f] = cnt +1    

    result = 0
    for k in visited:
        result += visited[k]

    return result


for _ in range(M):
    my, friend = map(int, input().split())
    graph[my].append(friend)
    graph[friend].append(my)

resultvalues = [0] * (N + 1)
for dic in graph:
    value = bfs(graph, dic)
    resultvalues[dic] = value


print(resultvalues.index(min(resultvalues[1:])))

