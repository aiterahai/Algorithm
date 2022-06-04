from math import sqrt, ceil

n, m = map(int, input().split())
prime_num = [True for i in range(1000001)]
prime_num[1] = False
for i in range(2, ceil(sqrt(m)) + 1):
    if(prime_num[i] == True):
        for j in range(2 * i, 1000001, i):
            prime_num[j] = False
for i in range(n, m+1):
    if(prime_num[i] == True): print(i)