def dfs(K):
    if K == L:
        temp = visit.count("a") + visit.count("e") + visit.count("i") + visit.count("o") + visit.count("u")
        if temp < 1 or K - temp < 2: return
        print("".join(map(str, visit)))
    else:
        for i in board:
            if K and visit[-1] > i or i in visit: continue
            visit.append(i)
            dfs(K + 1)
            visit.pop()

L, C = map(int, input().split())
board = sorted(input().split())
visit = []
dfs(0)