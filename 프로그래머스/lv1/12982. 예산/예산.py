def solution(d, budget):
    d, answer = sorted(d, reverse=True), 0
    while d and budget >= d[-1]: budget, answer = budget - d.pop(), answer + 1
    return answer