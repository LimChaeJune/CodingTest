from collections import deque


def bfs(place):
    start = []
    pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append((i, j))

    for st in start:
        # 방문처리
        visited = [[False for _ in range(5)] for _ in range(5)]
        # 거리처리
        guree = [[0 for _ in range(5)] for _ in range(5)]

        queue = deque()
        queue.append((st[0], st[1]))
        # 첫 큐에 넣을 때
        visited[st[0]][st[1]] = True

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                dx = x + pos[i][0]
                dy = y + pos[i][1]

                if 0 <= dx < 5 and 0 <= dy < 5 and visited[dx][dy] == False:
                    if place[dx][dy] == 'O':
                        queue.append((dx, dy))
                        visited[dx][dy] = True
                        guree[dx][dy] = guree[x][y] + 1

                    elif place[dx][dy] == 'P' and guree[x][y] <= 1:
                        return 0

    return 1


def solution(places):

    answer = []

    # 대기실 개수
    for place in places:
        answer.append(bfs(place))

    return answer
