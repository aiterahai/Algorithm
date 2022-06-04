from collections import deque
from sys import stdin
iter = int(stdin.readline())
for i in range(iter):
    count = 1
    n, m = map(int, stdin.readline().split())
    deck = deque(map(int, stdin.readline().split()))
    while(1):
        if m < 0: m = n - 1;
        if(deck[0] == max(deck) and m == 0):
            print(count)
            break;
        elif(deck[0] == max(deck)):
            deck.popleft()
            m -= 1
            n -= 1
            count += 1
        else:
            deck.append(deck.popleft())
            m -= 1