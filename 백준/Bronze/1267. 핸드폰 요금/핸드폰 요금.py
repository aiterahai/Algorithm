N = int(input())
board = list(map(int, input().split()))
Y, M = [((i//30)+1)*10 for i in board], [((i//60)+1)*15 for i in board]
if sum(M) >= sum(Y): print("Y", end=" ")
if sum(M) <= sum(Y): print("M", end=" ")
print(min(sum(M), sum(Y)))