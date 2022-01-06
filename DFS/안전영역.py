import sys
sys.setrecursionlimit(100000)

def dfs(x,y, rain, visited):
    if N <= x or x <= -1 or N <= y or y <= -1:
        return False
    
    if visited[x][y] == False and places[x][y] > rain:
        visited[x][y] = True

        dfs(x -1, y, rain, visited)
        dfs(x, y-1, rain, visited)
        dfs(x + 1, y, rain, visited)
        dfs(x, y+ 1, rain, visited)
        return True

    return False

N = int(input())

places = [[0 for col in range(N)] for row in range(N)]

for row in range(N):
    cols = list(map(int, input().split()))
    for col in range(len(cols)):
        places[row][col] = cols[col]

maxRain = max(map(max, places))

result = []
if (maxRain == 1):
    result.append(1)

for rain in range(1, maxRain):
    cnt = 0
    visited = [[False for col in range(N)] for row in range(N)]

    for i in range(N) :
        for j in range(N):
            if visited[i][j] == False:
                if dfs(i, j, rain, visited) == True:
                    cnt += 1

    result.append(cnt)

print(max(result))