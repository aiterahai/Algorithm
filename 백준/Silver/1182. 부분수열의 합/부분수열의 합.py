n, s = map(int, input().split())
arr = list(map(int, input().split()))
visitor = [0 for _ in range(n)]
count = 0
def dfs(k):
    global count
    for i in range(k, n):
        if visitor[i] == 1:
            continue
        else:
            visitor[i] = 1

            if sum([a*b for a,b in zip(visitor, arr)]) == s:
                count += 1
            dfs(i+1)
            visitor[i] = 0

dfs(0)
print(count)