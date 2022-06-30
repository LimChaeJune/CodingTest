from collections import deque
from itertools import combinations

N, M = map(int, input().split())
# 원본 보드
origin = []
# 바이러스 위치
virus = []


for i in range(N):
    row = list(map(int, input().split()))
    origin.append(row)
    for c in range(len(row)):
        if row[c] == 2:
            virus.append((i, c))


posx = [0, 0, 1, -1]
posy = [1, -1, 0, 0]


def bfs(visited, copyboard, queue):
    while queue:
        x, y, z = queue.popleft()

        for i in range(4):
            dx = x + posx[i]
            dy = y + posy[i]

            if 0 <= dx < N and 0 <= dy < N and visited[dx][dy] == False:
                if copyboard[dx][dy] == 0:
                    copyboard[dx][dy] = z+1
                    queue.append((dx, dy, z+1))
                    visited[dx][dy] = True
                elif copyboard[dx][dy] == 2:
                    copyboard[dx][dy] = 2
                    queue.append((dx, dy, z+1))
                    visited[dx][dy] = True

    maxtime = 0
    # 퍼지는 시간 계산
    for i in range(N):
        for j in range(N):
            if copyboard[i][j] == 0:
                return -1
            maxtime = max(copyboard[i][j], maxtime)

    # 아무것도 퍼지지 않았으면
    if maxtime == 2:
        return 0
    else:
        return maxtime - 3


result = 1e9
# M 조합으로 bfs 돌려서 확인
for comb in combinations(virus, M):
    queue = deque()
    # 1은 벽이고 2는 바이러스기 때문에 3부터 시작
    for i in comb:
        queue.append((i[0], i[1], 3))

    # 새 조합일때마다 board  copy
    copyboard = [item[:] for item in origin]

    visited = [[False for _ in range(N)]for _ in range(N)]
    for x, y in comb:
        visited[x][y] = True
    # bfs 작동
    bfsResult = bfs(visited, copyboard, queue)
    if bfsResult != -1:
        result = min(result, bfsResult)

# 다 퍼트리지 못할 때
if result == 1e9:
    result = -1

print(result)
