from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([(j,i) for i,j in enumerate(priorities)])
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location: break
    return answer