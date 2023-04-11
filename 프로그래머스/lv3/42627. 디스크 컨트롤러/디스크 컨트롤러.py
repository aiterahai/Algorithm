"""
file name: 디스크 컨트롤러.py

create time: 2023-04-11 13:55
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
import heapq

def solution(jobs):
    length = len(jobs)
    jobs = sorted(jobs, reverse=True)
    todo = []
    time = 0
    result = 0
    while jobs or todo:
        while jobs and time >= jobs[-1][0]:
            x, y = jobs.pop()
            heapq.heappush(todo, [y, x])
        if not todo: time += 1
        if todo:
            pt, it = heapq.heappop(todo)
            result += time - it + pt
            time += pt
    return result // length