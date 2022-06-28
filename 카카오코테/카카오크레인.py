def solution(board, moves):
    # 바구니
    contain = []
    answer = 0

    for i in moves:
        # 가장위에 있는거 바구니로
        for j in range(len(board)):
            if board[j][i-1] > 0:
                contain.append(board[j][i-1])
                board[j][i-1] = 0
                break

        # 바구니 검사
        if len(contain) >= 2:
            if contain[-1] == contain[-2]:
                contain.pop()
                contain.pop()
                answer += 2

    return answer
