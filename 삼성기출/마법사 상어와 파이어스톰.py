from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
board = []
fireStorm = []
boardsize = 2**N
for _ in range(boardsize):
    board.append(list(map(int, input().split())))

for item in list(map(int, input().split())):
    fireStorm.append(item)

posx = [0, 0, -1, 1]
posy = [1, -1, 0, 0]

for fire in fireStorm:
    # 격자 크기
    size = 2 ** fire

    curr_r = 0
    max_r = size
    curr_c = 0
    max_c = size
    # 격자 회전
    while True:
        newboard = []
        for r in range(curr_r, max_r):
            newboard.append(board[r][curr_c:max_c])

        # 회전
        rotated = list(zip(*newboard[::-1]))

        # 회전한 격자 board에 넣기
        for r in range(size):
            board[curr_r+r][curr_c:max_c] = rotated[r][:size]

        # 검색 범위 변경
        if max_c + size <= boardsize:
            curr_c += size
            max_c += size
        else:
            if max_r + size <= boardsize:
                curr_r += size
                max_r += size
                curr_c = 0
                max_c = size
            else:
                break

    rm_list = []
    # 인접한 얼음 확인
    for r in range(boardsize):
        for c in range(boardsize):
            if board[r][c] == 0:
                continue

            cnt = 0
            for i in range(4):
                dr = r + posx[i]
                dc = c + posy[i]

                if 0 <= dr < boardsize and 0 <= dc < boardsize:
                    if board[dr][dc] > 0:
                        cnt += 1
            if cnt < 3:
                rm_list.append((r, c))

    for x, y in rm_list:
        board[x][y] -= 1

result_size = 0


def bfs(st_x, st_y):
    # 처음 시작지점 +1
    cnt = 1
    visited = [[False for _ in range(boardsize)]for _ in range(boardsize)]
    queue = deque()
    queue.append((st_x, st_y))
    visited[st_x][st_y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            dx = x + posx[i]
            dy = y + posy[i]
            if 0 <= dx < boardsize and 0 <= dy < boardsize and board[dx][dy] > 0 and visited[dx][dy] == False:
                visited[dx][dy] = True
                queue.append((dx, dy))
                cnt += 1

    return cnt


result_sum = 0
for i in range(boardsize):
    result_sum += sum(board[i])

# for bo in board:
#   print(bo)
#   print()

result_cnt = 0
for x in range(boardsize):
    for y in range(boardsize):
        if board[x][y] == 0:
            continue

        result_cnt = max(result_cnt, bfs(x, y))
        if result_cnt == boardsize ** 2:
            break

print(result_sum)
print(result_cnt)
