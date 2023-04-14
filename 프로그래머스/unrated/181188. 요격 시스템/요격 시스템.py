def solution(targets):
    targets = sorted(targets, key = lambda x : (x[1], x[0]), reverse=True)
    
    answer = 0
    e = 0
    while targets:
        x, y = targets.pop()
        if x < e: continue
        answer += 1
        e = y

    return answer