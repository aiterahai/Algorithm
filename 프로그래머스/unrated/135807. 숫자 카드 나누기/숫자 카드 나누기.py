from math import gcd

def solution(arrayA, arrayB):
    
    A, B = arrayA.copy(), arrayB.copy()
    
    answer = 0
    
    while len(arrayA) != 1: arrayA.append(gcd(arrayA.pop(), arrayA.pop()))
    while len(arrayB) != 1: arrayB.append(gcd(arrayB.pop(), arrayB.pop()))
    
    print([i % arrayA[0] for i in B].count(0), arrayA)
    print([i % arrayB[0] for i in A].count(0), arrayB)
    
    if not [i % arrayA[0] for i in B].count(0): answer = arrayA[0]
    if not [i % arrayB[0] for i in A].count(0): answer = max(answer, arrayB[0])
    
    return answer