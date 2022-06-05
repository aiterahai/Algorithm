n = int(input())
up, left, right = [False for i in range(n)], [False for i in range(2*n-1)], [False for i in range(2*n-1)]
count = 0
def dfs(k):
    global count
    if k == n:
        count += 1
        return
    for i in range(n):
        if not(up[i] or left[k+i] or right[k-i+n-1]):
            up[i] = left[k+i] = right[k-i+n-1] = True
            dfs(k+1)
            up[i] = left[k+i] = right[k-i+n-1] = False
dfs(0)
print(count)