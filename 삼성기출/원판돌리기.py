import sys
from collections import deque


input = sys.stdin.readline
N, M, T = map(int, input().split())

circle = [deque(int(x) for x in input().split()) for _ in range(N)]
rtDto = [[int(x) for x in input().split()] for _ in range(T)]


def circleRotate(num, flag):
    if flag == 0:
        circle[num].rotate()
    elif flag == 1:
        circle[num].rotate(-1)


for i in range(len(rtDto)):
    # 번호가 x의 배수의 원판 (index라 +1 해줘야함)
    # 방향 d0 -> 시계 d1 -> 반시계 k 만큼 반복
    x, d, k = rtDto[i]

    check = 0
    for j in range(N):
        check += sum(circle[j])
        if (j+1) % x == 0:
            for _ in range(k):
                circleRotate(j, d)

    if check > 0:
        removeN = []

        # 같으 원
        for r in range(N):
            for c in range(M-1):
                if circle[r][c] != 0 and circle[r][c+1] != 0 and circle[r][c] == circle[r][c+1]:
                    removeN.append((r, c))
                    removeN.append((r, c+1))
            if circle[r][0] != 0 and circle[r][-1] != 0 and circle[r][-1] == circle[r][0]:
                removeN.append((r, 0))
                removeN.append((r, M-1))

        for c in range(M):
            for r in range(N-1):
                if circle[r][c] != 0 and circle[r+1][c] != 0 and circle[r+1][c] == circle[r][c]:
                    removeN.append((r+1, c))
                    removeN.append((r, c))

        removeN = list(set(removeN))

        # 원판에 수가 있다면 지우기
        if len(removeN):
            for rm in removeN:
                dr, dc = rm[0], rm[1]
                circle[dr][dc] = 0
        else:
            avgsum = 0
            zerosum = 0
            for i in range(N):
                avgsum += sum(circle[i])
                zerosum += circle[i].count(0)
            avg = avgsum / (N * M - zerosum)

            for i in range(N):
                for j in range(M):
                    if circle[i][j] != 0 and circle[i][j] > avg:
                        circle[i][j] -= 1
                    elif circle[i][j] != 0 and circle[i][j] < avg:
                        circle[i][j] += 1

    else:
        break

result = 0
for i in range(N):
    result += sum(circle[i])

print(result)
