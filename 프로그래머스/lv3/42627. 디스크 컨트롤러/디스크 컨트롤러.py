"""
file name: 디스크 컨트롤러.py

create time: 2023-04-11 13:55
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
import heapq
def solution(jobs):
    length, jobs, todo, time, result = len(jobs), sorted(jobs, reverse=True), [], 0, 0
    while jobs or todo:
        while jobs and time >= jobs[-1][0]: heapq.heappush(todo, [jobs[-1][1], jobs.pop()[0]])
        if todo:
            pt, it = heapq.heappop(todo)
            result, time = result + time - it + pt, time + pt
        else: time += 1
    return result // length

print(solution([[0, 3], [1, 9], [2, 6]]))