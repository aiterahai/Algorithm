A, B = input(), input()
board_A, board_B = [0] * 26, [0] * 26
count = 0
for i in A: board_A[ord(i) - 97] += 1
for i in B: board_B[ord(i) - 97] += 1
for i in range(26): count += abs(board_A[i] - board_B[i])
print(count)