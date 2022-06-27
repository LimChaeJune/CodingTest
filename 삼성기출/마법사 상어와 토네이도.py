N = int(input())

# 원본
board = []

# 원본 생성
for i in range(N):
    board.append(list(map(int, input().split())))

# 토네이도 (왼쪽)
left = [(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02), (-1, 1, 0.01),
        (1, 1, 0.01),                 (1, -1, 0.1), (-1, -1, 0.1), (0, -2, 0.05), (0, -1, 0)]
# 토네이도 (아래)
down = [(-y, x, z) for x, y, z in left]
# 토네이도 (오른쪽)
right = [(x, -y, z) for x, y, z in left]
# 토네이도 (위)
up = [(y, x, z) for x, y, z in left]

late = [left, down, right, up]

# 현재지점 (처음에는 N의 절반)
x = [N//2, N//2]
# 현재 방향
curr_x = 0
# 방향별 (왼,아,오,위)
pos = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 직선 길이
curr_len = 0
# 현재 방향 증가 길이
max_len = 2
# 나간 모래
answer = 0

# 방향 전환


def direct():
    global curr_x, curr_len, max_len

    if curr_len == max_len // 2 or curr_len == max_len:
        curr_x = (curr_x+1) % 4
        if curr_len == max_len and curr_len != N:
            curr_len = 0
            max_len += 2

# 모래 계산


def tonado():
    global answer, curr_len, x
    mypos = pos[curr_x]
    y = [(x[0] + mypos[0]), (x[1] + mypos[1])]
    # 빠져나간 양
    remain = 0

    # 흩날림 처리
    for fx, fy, z in late[curr_x]:
        dx = y[0] + fx
        dy = y[1] + fy

        # alpha
        if z == 0:
            sand = board[y[0]][y[1]] - remain
        else:
            # 현재 퍼센트 모래
            sand = int(board[y[0]][y[1]] * z)
            remain += sand

        # 범위 안이면 격자에 포함시킴
        if (0 <= dx < N and 0 <= dy < N):
            board[dx][dy] += sand
        else:
            answer += sand

    board[y[0]][y[1]] = 0
    curr_len += 1
    x = y

    # 방향전환 확인
    direct()


while True:
    if x[0] == 0 and x[1] == 0:
        break
    tonado()


print(answer)
