def solution(board, moves):
    nb = [[] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]: nb[j].append(board[i][j])
    board = [i[::-1] for i in nb]
    total = []
    result = 0
    for i in moves:
        if board[i - 1]: total.append(board[i - 1].pop())
        if len(total) < 2: continue
        if total[-1] == total[-2]: total.pop();total.pop();result += 2
    return result