from collections import Counter
def solution(participant, completion): 
    P = Counter(participant)
    C = Counter(completion)
    P.subtract(C)
    return P.most_common(1)[0][0]