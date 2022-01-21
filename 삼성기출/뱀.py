from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

graph = [[0 for j in range(N+1)] for i in range(N+1)]
poses = {}

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x][y] = 1

for _ in range(int(input())):
    cnt, way = map(str,input().split()) 
    poses[int(cnt)] = way

def headChange(way, hw):        
    if way == 'L':
        dhw = hw -1
        if dhw < 0:
            hw = 3
        else: hw = dhw
    if way == 'D':
        dhw = hw + 1
        if dhw > 3:
            hw = 0
        else: hw = dhw

    return hw

def bfs():        
    result = 1
    headway = 0
    snake = deque()

    snake.append((1,1))

    while True:
        x, y = snake[-1]
        
        dx = x + pos[headway][0]
        dy = y + pos[headway][1]    

        if N < dx or dx < 1 or N < dy or dy < 1 or (dx,dy) in snake:
            print(result)
            exit()

        if graph[dx][dy] == 0:            
            snake.popleft() 
        else:
            graph[dx][dy] = 0

        if result in poses:
            headway = headChange(poses[result], headway)            
        
        result += 1
        snake.append((dx,dy))

    


pos = [(0,1),(1,0),(0,-1),(-1,0)]

bfs()