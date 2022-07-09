from collections import deque

# N 보드 M
n, m, k = map(int, input().split())

board = [[0 for _ in range(n)]for _ in range(n)]

for r in range(n):
    ipt = list(map(int, input().split()))
    for c in range(len(ipt)):
        if ipt[c] == 1:
            board[r][c] = -1

taxix, taxiy = map(int, input().split())
taxix = taxix - 1
taxiy = taxiy - 1

customer = []
for i in range(m):
    a, b, c, d = map(int, input().split())
    customer.append([a-1, b-1, c-1, d-1])

posx = [0, 0, 1, -1]
posy = [1, -1, 0, 0]

# 최단거리 찾기


def min_len(st_x, st_y):
    queue = deque()
    queue.append((st_x, st_y))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[st_x][st_y] = 1
    result = []
    min = 9999

    while queue:
        x, y = queue.popleft()
        if visited[x][y] > min:
            break

        for cus in customer:
            if x == cus[0] and y == cus[1]:
                result.append(cus)
                min = visited[x][y]

        for i in range(4):
            dx = x + posx[i]
            dy = y + posy[i]

            if 0 <= dx < n and 0 <= dy < n and board[dx][dy] != -1 and visited[dx][dy] == 0:
                visited[dx][dy] = visited[x][y] + 1
                queue.append((dx, dy))

    if len(result) > 0:
        result.sort(key=lambda x: (x[0], x[1]))
        return [result[0], visited[result[0][0]][result[0][1]]-1]
    else:
        return [-1, -1]


def active(st_x, st_y, fns_x, fns_y):
    queue = deque()
    queue.append((st_x, st_y))

    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[st_x][st_y] = 1
    while queue:
        x, y = queue.popleft()

        if x == fns_x and y == fns_y:
            return visited[x][y] - 1

        for i in range(4):
            dx = x + posx[i]
            dy = y + posy[i]

            if 0 <= dx < n and 0 <= dy < n and board[dx][dy] != -1 and visited[dx][dy] == 0:
                queue.append((dx, dy))
                visited[dx][dy] = visited[x][y] + 1

    # 목적지에 도착하지 못할 때
    return -1


for i in range(len(customer)):
    minresult = min_len(taxix, taxiy)

    # 승객을 태우러 갈수 없을 때
    if minresult[1] == -1:
        print(-1)
        break

    taxix, taxiy = minresult[0][0], minresult[0][1]
    # 최단거리 손님한테 갈 기름이 없을 때
    if minresult[1] > k:
        print(-1)
        break
    else:
        k -= minresult[1]

        st_x, st_y, fns_x, fns_y = minresult[0]
        target_oil = active(st_x, st_y, fns_x, fns_y)

        if target_oil == -1:
            print(-1)
            break
        elif k >= target_oil:
            k += target_oil
            taxix, taxiy = fns_x, fns_y
            # 운행 종료하면 삭제
            customer.remove(minresult[0])
        # 목적지까지 도달하거나 도달 못했을 때
        else:
            print(-1)
            break

if len(customer) == 0:
    print(k)
