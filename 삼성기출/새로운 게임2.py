from collections import deque
N, K = map(int, input().split())
# 벽 위치
board = []
# 말 쌓아놓는 위치
horse_board = [[deque() for _ in range(N)] for _ in range(N)]
# 말 위치
horse = []

pos = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for i in range(N):
    board.append(list(map(int, input().split())))

for i in range(K):
    x, y, z = map(int, input().split())
    horse.append((x-1, y-1, z-1))
    horse_board[x-1][y-1].append(i)


def dir_reverse(dir):
    if dir == 0 or dir == 2:
        dir += 1
    else:
        dir -= 1
    return dir

# for b in horse_board:
#   print(b)
# print()


result = 1
while result <= 1001:
    for i in range(K):
        x, y, z = horse[i]

        dx = x + pos[z][0]
        dy = y + pos[z][1]

        if 0 <= dx < N and 0 <= dy < N and board[dx][dy] != 2:
            # 흰색 인 경우 그냥 이동
            if board[dx][dy] == 0:
                row = deque()

                for _ in range(len(horse_board[x][y])):
                    idx = horse_board[x][y].pop()
                    row.appendleft(idx)
                    # 위치 초기화
                    horse[idx] = (dx, dy, horse[idx][2])
                    if idx == i:
                        break

                for r in row:
                    horse_board[dx][dy].append(r)

            elif board[dx][dy] == 1:
                row = deque()

                for _ in range(len(horse_board[x][y])):
                    idx = horse_board[x][y].pop()
                    row.append(idx)
                    # 위치 초기화
                    horse[idx] = (dx, dy, horse[idx][2])
                    if idx == i:
                        break

                for r in row:
                    horse_board[dx][dy].append(r)

            horse[i] = [dx, dy, z]
        else:
            rv_dir = dir_reverse(horse[i][2])

            dx = x + pos[rv_dir][0]
            dy = y + pos[rv_dir][1]

            horse[i] = (x, y, rv_dir)

            # 또 체스판을 벗어나거나 파란색인지 확인
            if 0 <= dx < N and 0 <= dy < N and board[dx][dy] != 2:
                if board[dx][dy] == 0:
                    row = deque()

                    for _ in range(len(horse_board[x][y])):
                        idx = horse_board[x][y].pop()
                        row.appendleft(idx)
                        # 위치 초기화
                        horse[idx] = (dx, dy, horse[idx][2])
                        if idx == i:
                            break

                    for r in row:
                        horse_board[dx][dy].append(r)

                elif board[dx][dy] == 1:
                    row = deque()

                    for _ in range(len(horse_board[x][y])):
                        idx = horse_board[x][y].pop()
                        row.append(idx)
                        # 위치 초기화
                        horse[idx] = (dx, dy, horse[idx][2])
                        if idx == i:
                            break

                    for r in row:
                        horse_board[dx][dy].append(r)

                horse[i] = [dx, dy, rv_dir]

        for iy in range(K):
            x, y, z = horse[iy]
            if len(horse_board[x][y]) > 3:
                print(result)
                exit(0)

    # for b in horse_board:
    #   print(b)
    # print()

    # 턴 종료 및 계산
    result += 1

print(-1)
