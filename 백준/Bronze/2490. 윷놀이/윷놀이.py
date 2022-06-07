from sys import stdin
for i in range(3):
    temp = map(int, stdin.readline().split())
    zero_cnt = 0
    for i in temp:
        if i == 0: zero_cnt += 1
    if zero_cnt == 0: print("E")
    elif zero_cnt == 1: print("A")
    elif zero_cnt == 2: print("B")
    elif zero_cnt == 3: print("C")
    elif zero_cnt == 4: print("D")