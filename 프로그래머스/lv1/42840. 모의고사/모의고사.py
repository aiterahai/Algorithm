def solution(answers):
    result = [0, 0, 0]
    pattern = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(answers)):
        if answers[i] == pattern[0][i % 5]: result[0] += 1
        if answers[i] == pattern[1][i % 8]: result[1] += 1
        if answers[i] == pattern[2][i % 10]: result[2] += 1
    answer = [idx + 1 for idx, value in enumerate(result) if value == max(result)]
    
    return answer