n, m = map(int, input().split())
visitors = sorted(map(int, input().split()))
visited = []

def dfs(k):
    if(len(visited) == m):
        print(' '.join(map(str, visited)))
    else:
        for i in visitors:
            if i in visited:
                continue
            visited.append(i)
            dfs(k+1)
            visited.pop()

dfs(0)