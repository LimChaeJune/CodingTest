# def Alpabet(graph, row, col, visitalpa, checkresult):        
#     global result    

#     result = max(result, checkresult)    
        
#     for step in steps:      
#         x = row + step[0]
#         y = col + step[1]         
#         if 0 <= x < Rows and 0 <= y < Cols and graph[x][y] not in visitalpa:
#             visitalpa.add(graph[x][y])
#             Alpabet(graph, x, y, visitalpa, checkresult + 1)                               
#             visitalpa.remove(graph[x][y])
    


# Rows, Cols = map(int,input().split()) 

# board = [[0 for i in range(Cols)] for j in range(Rows)] 

# steps = [(0,1),(0,-1),(-1,0),(1,0)]

# visitalpa = set()

# result = 1

# for row in range(0,Rows):
#      alpa = input()
#      for col in range(0, Cols):
#          board[row][col] = alpa[col]

# visitalpa.add(board[0][0])
# Alpabet(board, 0, 0, visitalpa, result)
# print(result)

# ----------------- 시간초과로 다시 ㅜㅜㅜㅜㅜㅜ ----------------

# 이거 넣어야지 시간 초과 안나옴 https://www.acmicpc.net/problem/15552 참고
import sys
sys.setrecursionlimit(10**9)
input = lambda:sys.stdin.readline().strip()

r,c = map(int,input().split())
graph = [list(map(lambda a : ord(a)-65,input())) for _ in range(r)]
visited = [0]*26

steps = [(0,1),(0,-1),(-1,0),(1,0)]

def dfs(x,y,cnt):
    global ans

    ans = max(ans,cnt)    
        
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]

        if 0 <= nx < r and 0 <= ny < c and visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            dfs(nx,ny,cnt+1)
            visited[graph[nx][ny]] = 0

ans  = 1

visited[graph[0][0]] = 1
dfs(0, 0, ans)

print(ans)