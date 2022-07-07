from collections import deque

# N 보드, M 승객 갯수, oil 연료
N, M, oil = map(int, input().split())
board = []
taxix, taxiy = []
customer = []
visited = []

for _ in range(N):
    board.append(list(map(int, input().split())))

taxix, taxiy = map(int, input().split())

for _ in range(M):
    st_x, st_y, fns_x, fns_y = map(int, input().split())
    customer.append([[st_x, st_y], [fns_x, fns_y]])


def min
