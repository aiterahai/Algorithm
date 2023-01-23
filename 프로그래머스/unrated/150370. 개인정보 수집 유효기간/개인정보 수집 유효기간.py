def solution(today, terms, privacies):
    today = list(map(int, today.split(".")))
    d = dict()
    for i in terms:
        i, j = i.split()
        d[i] = int(j)
    privacies = [[list(map(int, i[:-2].split("."))), d[i[-1]]] for i in privacies]
    for i, j in enumerate(privacies):
        privacies[i][0][1] += privacies[i][1]
        privacies[i] = privacies[i][0]
        privacies[i][0] += (privacies[i][1] - 1) // 12
        privacies[i][1] = (privacies[i][1] - 1) % 12 + 1
    return [i + 1 for i, j in enumerate(privacies) if compare(today, j)]

def compare(today, day):
    today = list(map(str, today))
    
    day = list(map(str, day))
    today[1], today[2], day[1], day[2] = today[1].zfill(2), today[2].zfill(2), day[1].zfill(2), day[2].zfill(2)
    today, day = "".join(today), "".join(day)
    print(today, day)
    return int(today) >= int(day)