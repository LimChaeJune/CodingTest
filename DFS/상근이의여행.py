import sys
sys.setrecursionlimit(100000)

from collections import deque
from collections import defaultdict


T = int(input())


for j in range(T):

    graph = defaultdict(list)
    N, M = list(map(int, input().split()))

    for i in range(M):
        st, fns = list(map(int,input().split()))
        graph[st].append(fns)
        graph[fns].append(st)

        visted = [0] * (N+1)


    def dfs(idx, cnt):
        visted[idx] = 1

        for i in graph[idx]:            
            if(visted[i] == 0):                
                cnt = dfs(i, cnt+1)

        return cnt
    
    print(dfs(1,0))
        