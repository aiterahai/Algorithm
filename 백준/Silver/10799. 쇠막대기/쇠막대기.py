board, count, answer = input(), 0, 0
for i in range(len(board)):
    if board[i] == "(": count += 1; continue
    if board[i-1] == "(": answer, count = answer + count - 1, count - 1
    else: answer, count = answer + 1, count - 1
print(answer)