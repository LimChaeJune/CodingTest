import sys
input = sys.stdin.readline
N, K = map(int, input().split()) 

if K < 5:
    print(0)
    exit()

if K == 26:
    print(N)
    exit()

words = [set(sys.stdin.readline().rstrip()) for _ in range(N)]

visited = [False] * 26
for i in ['a','n','t','i','c']:
    visited[ord(i) - ord('a')] = True

result = 0

def dfs(idx, cnt):
    global result    

    if cnt == K:
        thiscnt = 0
        for wr in words:
            check = True
            for ch in wr:
                if not visited[ord(ch) - ord('a')]:
                    check = False
                    break
            
            if check:
                thiscnt += 1
        result = max(result, thiscnt)
        return
    
    for i in range(idx, 26):
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)   
            visited[i] = False


dfs(0, 5)
print(result)