def solution(citations):
    citations.sort(reverse=True)
    M = 0
    for i in citations:
        if i > M:
            M += 1
    return M