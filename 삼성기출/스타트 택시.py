from collections import deque

# N 보드, M 승객 갯수, oil 연료
N, M, oil = map(int, input().split())
board = []


for _ in range(N):
    board.append(list(map(int, input().split())))

# 현재 택시 위치
taxi_x, taxi_y = map(int, input().split())
curr_taxi = [taxi_x, taxi_y]

# 도착지 목적지 처리
for i in range(2, M):
    st_x, st_y, fns_x, fns_y = map(int, input().split())
    board[st_x-1][st_y-1] = i
    board[fns_x-1][fns_y-1] = -i


posx = [1, -1, 0, 0]
posy = [0, 0, 1, -1]


def find_customer():
    cus = []
    queue = deque()
    queue.append(curr_taxi[0], curr_taxi[1], 0)
    # 가장 가까운 손님 찾기
    while queue:
        x, y, le = queue.pop()
        # 목적지는 어차피 음수라 안찾아짐
        if board[x][y] > 1:
            cus = [x, y, le, board[x][y]]
            board[x][y] = 0
            break

        for i in range(4):
            dx = x + posx[i]
            dy = y + posy[y]

            if 0 <= dx < N and 0 <= dy < N:
                if board[dx][dy] != 1:
                    queue.append((dx, dy, le+1))

    return cus


def active(z):
    visited = [[False for _ in range(N)]for _ in range(N)]

    queue = deque()
    queue.append(curr_taxi[0], curr_taxi[1], 0)
    while queue:
        x, y, oil = queue.pop()
        # 목적지는 어차피 음수라 안찾아짐
        if abs(board[x][y]) == z:
            return oil

        for i in range(4):
            dx = x + posx[i]
            dy = y + posy[y]

            if 0 <= dx < N and 0 <= dy < N:
                if board[dx][dy] != 1:
                    queue.append((dx, dy, oil+1))


result = -1
# 오일이 남아있으면
while oil > 0:
    cus = find_customer()
    print(cus)
    # 손님을 찾아가는 길이 남은 오일보다 길면
    if cus[2] > oil:
        result = -1
    else:
        # 출발지까지 오일 감소
        oil -= cus[2]
        # 손님 위치에서 시작
        curr_taxi = [cus[0], cus[1]]

        playoil = active(cus[3])
