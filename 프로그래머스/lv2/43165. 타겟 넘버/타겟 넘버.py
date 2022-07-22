answer = 0
def dfs(K, value, numbers, target):
    global answer
    if K == len(numbers):
        if target == value: answer += 1
        return
    dfs(K+1, value + numbers[K], numbers, target)
    dfs(K+1, value - numbers[K], numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer