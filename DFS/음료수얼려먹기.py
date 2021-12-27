def dfs(x,y):
    if N <= x <= -1 or M <= y <= -1:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x -1, y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y+ 1)
        return True

    return False

N, M = map(int,input().split()) 

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


result = 0

for i in range(N) :
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)