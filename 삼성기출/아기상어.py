from collections import deque

N = int(input())

graph = [[0 for i in range(N)] for _ in range(N)]

shark = []
fishes = []

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(len(row)):
        if row[j] == 9:
            shark.append((i,j))
        elif 0 < row[j] < 7:
            fishes.append((row[j], (i,j)))

queue = deque()
queue.append((shark[0],0))

while queue:
    x,y, T = queue.popleft()
    
    