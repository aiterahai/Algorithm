from sys import stdin

count = 0
for _ in range(int(stdin.readline())):
    read = stdin.readline().rstrip()
    if read == "ENTER":
        board = set()
        continue
    if read in board: continue
    else:
        board.add(read)
        count += 1

print(count)