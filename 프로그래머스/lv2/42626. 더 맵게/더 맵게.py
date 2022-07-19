import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        if scoville[0] >= K: return answer
        answer += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
    if K <= heapq.heappop(scoville): return answer
    return -1