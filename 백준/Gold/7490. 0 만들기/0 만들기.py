from sys import stdin

def dfs(K):
    if K == N + 1:
        if eval("".join(visit)) == 0: result.append("".join(visit))
        return
    for i in ["+", "-", ""]:
        visit.append(i)
        visit.append(str(K))
        dfs(K + 1)
        visit.pop()
        visit.pop()
for _ in range(int(stdin.readline())):
    result = []
    N = int(stdin.readline())
    visit = ["1"]
    dfs(2)
    for i in range(len(result)):
        temp = ["1"]
        for j in range(1, len(result[i])):
            if result[i][j].isdigit() and result[i][j - 1].isdigit(): temp.append(" ")
            temp.append(str(result[i][j]))
        result[i] = "".join(temp)
    print(*sorted(result), sep="\n")
    print()