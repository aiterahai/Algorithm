from sys import stdin

N, K, answer, number, nine = *map(int, stdin.readline().split()), 0, 1, 9

while K > number * nine:
    K -= (number * nine)
    answer += nine
    number += 1
    nine = nine * 10

print(-1 if (answer+1) + (K-1) // number > N else str((answer + 1) + (K - 1) // number)[(K - 1) % number])