import heapq

xs,ys = map(int, input().split())
xe,ye = map(int, input().split())

q = []
visited = []
nodes = []

nodes.append((xs,ys,False))
nodes.append((xe,ye,False))

graph = [[] for i in range(8)]

for i in range(0,5,2):
  dx1,dy1, dx2,dy2 = map(int,input().split())
  nodes.append((dx1,dy1,True))
  nodes.append((dx2,dy2,True))    
  graph[2+i].append((10, 2+i+1))
  graph[2+i+1].append((10, 2+i))  


for i in range(len(nodes)):
  for j in range(len(nodes)):    
    graph[i].append((abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1]), j))    

heapq.heappush(q, (0,0))
answer = 0
while True:
  v, node = heapq.heappop(q)  

  if nodes[node][0] == xe  and nodes[node][1] == ye:
    answer = v
    break

  if (nodes[node][0], nodes[node][1]) in visited:
    continue

  visited.append((nodes[node][0], nodes[node][1]))           

  for i in graph[node]:
    heapq.heappush(q, (v+i[0],i[1]))


print(answer)