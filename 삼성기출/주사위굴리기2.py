from collections import deque

N, M, K = map(int, input().split())

# 뒤, 왼, 위, 오, 앞, 밑
dice = [2, 4, 1, 3, 5, 6]
board = []
visited_board = [[0 for _ in range(M)] for _ in range(N)]
# 현재 주사위가 구르는 방향 오른쪽, 아래, 왼쪽, 위
direction = 0
pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(N):
    board.append(list(map(int, input().split())))

# 주사위 굴리기 (방향, 현재 주사위 값)


def get_newdice(dir, curr_dice):
    newdice = []
    if dir == 0:
        newdice = [curr_dice[0], curr_dice[5],   curr_dice[1],
                   curr_dice[2], curr_dice[4], curr_dice[3]]
    elif dir == 2:
        newdice = [curr_dice[0], curr_dice[2], curr_dice[3],
                   curr_dice[5], curr_dice[4], curr_dice[1]]
    elif dir == 1:
        newdice = [curr_dice[5], curr_dice[1], curr_dice[0],
                   curr_dice[3], curr_dice[2], curr_dice[4]]
    elif dir == 3:
        newdice = [curr_dice[2], curr_dice[1], curr_dice[4],
                   curr_dice[3], curr_dice[5], curr_dice[0]]

    return newdice


def dir_reverse(dir):
    if dir < 2:
        dir += 2
    else:
        dir -= 2
    return dir


def dir_rotate(dir, reverse):
    if reverse == False:
        dir = (dir + 1) % 4
    else:
        if dir == 0:
            dir = 3
        else:
            dir = (dir - 1)
    return dir


def getpoint(st_x, st_y):
    global visited_board

    visited = []
    queue = deque()
    queue.append((st_x, st_y))
    visited.append((st_x, st_y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + pos[i][0]
            dy = y + pos[i][1]

            if 0 <= dx < N and 0 <= dy < M and (dx, dy) not in visited:
                if board[st_x][st_y] == board[dx][dy]:
                    queue.append((dx, dy))
                    visited.append((dx, dy))

    value = board[st_x][st_y] * len(visited)
    for x, y in visited:
        visited_board[x][y] = value


# 현재 주사위 위치
curr_x, curr_y = 0, 0
result = 0

for _ in range(K):
    dx = curr_x + pos[direction][0]
    dy = curr_y + pos[direction][1]

    # 주사위가 범위를 벗어나면 다시
    if 0 > dx or dx >= N or 0 > dy or dy >= M:
        direction = dir_reverse(direction)
        dx = curr_x + pos[direction][0]
        dy = curr_y + pos[direction][1]

    dice = get_newdice(direction, dice)

    # 포인트 적립
    if visited_board[dx][dy] > 0:
        result += visited_board[dx][dy]
    else:
        getpoint(dx, dy)
        result += visited_board[dx][dy]

    # 방향전환
    if board[dx][dy] > dice[5]:
        direction = dir_rotate(direction, True)
    elif board[dx][dy] < dice[5]:
        direction = dir_rotate(direction, False)

    curr_x, curr_y = dx, dy

print(result)
