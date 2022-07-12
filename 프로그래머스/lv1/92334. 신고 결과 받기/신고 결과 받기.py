from collections import Counter

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    reports = Counter([i.split()[1] for i in set(report)])
    reports = [i for i in reports if reports[i] >= k]
    for i in set(report):
        if i.split()[1] in reports: answer[id_list.index(i.split()[0])] += 1
    return answer