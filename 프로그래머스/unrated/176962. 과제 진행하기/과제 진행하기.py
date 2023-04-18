"""
file name: 176962.py

create time: 2023-04-18 19:46
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
def solution(plans):
    plans = sorted([[int(b.split(":")[0]) * 60 + int(b.split(":")[1]), int(c), a] for a, b, c in plans], reverse=True)
    Q = []
    answer = []
    time = 0
    while Q or plans:
        if not Q: time += 1

        if Q:
            Q[-1][1] -= 1
            time += 1

        if Q and Q[-1][1] == 0:
            answer.append(Q.pop()[2])

        if plans and plans[-1][0] <= time:
            Q.append(plans.pop())
            continue
    
    return answer