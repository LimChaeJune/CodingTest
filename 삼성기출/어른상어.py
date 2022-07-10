import sys
from collections import defaultdict
input = sys.stdin.readline

# k - 초기냄새
N, M, k = map(int, input().split())

# 우선순위 포지션
shark_prirory = [[] for _ in range(M)]
# 상어 위치
shark_pos = defaultdict(list)

# 냄새 저장소
board = [[[] for _ in range(N)] for _ in range(N)]

for x in range(N):
    items = list(map(int, input().split()))
    for y in range(N):
        if items[y] > 0:
            shark_pos[items[y]-1] = [x, y]

# 현재 상어가 바라보고 있는 방향
shark_dir = []
for dir in list(map(int, input().split())):
    shark_dir.append(dir-1)

for x in range(M):
    for y in range(4):
        item = list(map(int, input().split()))
        newlist = []
        for cl in range(4):
            newlist.append(item[cl] - 1)
        shark_prirory[x].append(newlist)


posx = [-1, 1, 0, 0]
posy = [0, 0, -1, 1]
cnt = 0
while cnt < 1001:
    # 이동한 위치 확인을 위한 복사
    copyboard = [[[] for _ in range(N)] for _ in range(N)]

    # 냄새
    for key in shark_pos:
        pos = shark_pos[key]
        # 방귀 뿡
        board[pos[0]][pos[1]] = [key, k]

    # 방향 / 이동
    for key in shark_pos:
        pos = shark_pos[key]

        smell = []
        empty = []
        # 주위에 빈칸 있는지 확인
        for i in range(4):
            dx = pos[0] + posx[i]
            dy = pos[1] + posy[i]
            if 0 <= dx < N and 0 <= dy < N:
                if len(board[dx][dy]) == 0:
                    empty.append([dx, dy, i])
                elif board[dx][dy][0] == key:
                    smell.append([dx, dy, i])

        # print()
        # print('shark',key,'empty',empty)

        # 빈칸이 1이상이면 우선순위 따라서 방향전환
        if len(empty) > 0:
            # 빈칸이 2개이상이면 우선순위 점검
            if len(empty) > 1:
                # 현재바라보고있는 방향의 우선순위로 빈칸 검사
                flag = False
                for priority in shark_prirory[key][shark_dir[key]]:
                    if flag == True:
                        break
                    for emp in empty:
                        x, y, z = emp
                        if z == priority:
                            shark_dir[key] = z
                            copyboard[x][y].append(key)
                            flag = True
                            break
            else:
                x, y, z = empty[0]
                shark_dir[key] = z
                copyboard[x][y].append(key)
        # 빈칸이 없을 때
        else:
            # 냄새나는 곳이 여러곳 일 때
            if len(smell) > 1:
                flag = False
                for priority in shark_prirory[key][shark_dir[key]]:
                    if flag:
                        break
                    for sm in smell:
                        x, y, z = sm
                        if z == priority:
                            shark_dir[key] = z
                            copyboard[x][y].append(key)
                            flag = True
                            break
            else:
                x, y, z = smell[0]
                shark_dir[key] = z
                copyboard[x][y].append(key)

    # print()
    # print('copyboard',copyboard)
    # print()
    # print('smell', board)

    # 동일한 위치의 상어 확인 후 큰거 빼고 삭제

    # 냄새처리
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) > 0:
                idx, val = board[x][y]
                if val == 1:
                    board[x][y] = []
                else:
                    board[x][y][1] = val - 1

            if len(copyboard[x][y]) > 0:
                copyboard[x][y].sort()
                first = copyboard[x][y][0]
                shark_pos[first] = [x, y]
                for i in range(1, len(copyboard[x][y])):
                    target = copyboard[x][y][i]
                    del shark_pos[target]
    cnt += 1

    if len(shark_pos) == 1:
        break

if cnt == 1001:
    print(-1)
else:
    print(cnt)
