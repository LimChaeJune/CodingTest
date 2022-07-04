import sys
from collections import deque

input = sys.stdin.readline
# NxN 땅 / M 나무 갯수 / K 년수
N, M, K = map(int, input().split())

# 로봇이 넣는 양분
robots = []

# 양분
floor = [[5 for _ in range(N)]for _ in range(N)]
# 나무
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(N):
    robots.append(list(map(int, input().split())))

for _ in range(M):
    # 위치 , 나이
    x, y, z = map(int, input().split())
    # 작은 순서부터 정렬
    trees[x-1][y-1].append(z)


# 년도만큼 반복
for _ in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            addfloor = 0
            newdt = deque()
            for tree in trees[i][j]:
                if tree <= floor[i][j]:
                    floor[i][j] -= tree
                    newdt.append(tree+1)
                else:
                    addfloor += tree // 2
            trees[i][j] = newdt
            floor[i][j] += addfloor

    # 가을
    pos = [(0, 1), (1, 0), (-1, 0), (0, -1),
           (-1, 1), (-1, -1), (1, -1), (1, 1)]
    for x in range(N):
        for y in range(N):
            for tree in trees[x][y]:
                # 5의 배수
                if tree % 5 == 0:
                    for po in pos:
                        dx = x + po[0]
                        dy = y + po[1]

                        if 0 <= dx < N and 0 <= dy < N:
                            trees[dx][dy].appendleft(1)
            floor[x][y] += robots[x][y]

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])


print(answer)
