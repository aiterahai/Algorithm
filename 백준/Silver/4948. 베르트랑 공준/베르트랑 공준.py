from math import sqrt, ceil

prime_num = [True for i in range(246913)]
prime_num[1] = False
for i in range(2, ceil(sqrt(246913)) + 1):
    if(prime_num[i] == True):
        for j in range(2 * i, 246913, i):
            prime_num[j] = False

temp = int(input())
while(temp != 0):
    count = 0
    for i in range(temp + 1, 2*temp+1):
        if(prime_num[i]): count += 1
    print(count)
    temp = int(input())