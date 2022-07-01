N, M, H = map(int, input().split())
# 가로선 위치
board = [[False for _ in range(N+1)]for _ in range(H+1)]
for _ in range(M):
    s, t = map(int, input().split())
    board[s][t] = True

result = 4

# 사다리 타기


def check():
    # 열 별로 진행
    for i in range(1, N+1):
        # 지금 진행중인 열
        curr_k = i
        # 가로 확인
        for j in range(1, H+1):

            if board[j][curr_k] == True:
                curr_k += 1
            elif board[j][curr_k-1] == True:
                curr_k -= 1

        # 일치하지 않으면 바로 반환
        if curr_k != i:
            return False

    return True


def dfs(cnt):
    global result

    # 사다리 타서 바로 결과가 일치하면 반환
    if check():
        result = min(cnt, result)
        return

    else:
        # dfs 돌리는게 의미가 없으면 정지
        if (cnt+1 > result):
            return
        elif (cnt+1 > 3):
            return
        else:
            # 가로 사다리 놓기
            for r in range(1, H + 1):
                for c in range(1, N):
                    if board[r][c] == False:
                        if board[r][c-1] == False and board[r][c+1] == False:
                            board[r][c] = True
                            dfs(cnt+1)
                            # 다 돌린 이후 해제
                            board[r][c] = False


dfs(0)

print(-1 if result == 4 else result)
