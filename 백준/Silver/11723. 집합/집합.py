from sys import stdin

S = [False for i in range(21)]
M = int(stdin.readline())
for i in range(M):
    T = stdin.readline().split()
    if T[0] == "add": S[int(T[1])] = True
    elif T[0] == "check":
        if S[int(T[1])]: print("1")
        else: print("0")
    elif T[0] == "remove" and S[int(T[1])]: S[int(T[1])] = False
    elif T[0] == "toggle":
        if S[int(T[1])]: S[int(T[1])] = False
        else: S[int(T[1])] = True
    elif T[0] == "all": S = [True for i in range(21)]
    elif T[0] == "empty": S = [False for i in range(21)]