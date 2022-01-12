n = int(input())



def solution():
    for i in range(n - 1):                
        for j in range(len(graph[i])):                        
            if j == 0:
                graph[i+1][j] = graph[i][j] + graph[i+1][j]
            
            if j < len(graph[i]) - 1:
                graph[i+1][j+1] = max((graph[i][j] + graph[i+1][j+1]), (graph[i][j+1] + graph[i+1][j+1]))
            else:
                graph[i+1][j+1] = (graph[i][j] + graph[i+1][j+1])

    return print(max(graph[n-1]))
    
graph = []
# graph.append(int(input()))
for i in range(n):    
    j = list(map(int,input().split()))
    graph.append(j)

solution()


