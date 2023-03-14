def arrSum(A, B): return [a + b for a, b in zip(A, B)]

def solution(progresses, speeds):
    progresses, speeds = progresses[::-1], speeds[::-1]
    answer = []
    while progresses:
        t = 0
        while progresses and progresses[-1] >= 100:
            t += 1
            progresses.pop()
            speeds.pop()
        if t: answer.append(t)
        progresses = arrSum(progresses, speeds)
    
    return answer