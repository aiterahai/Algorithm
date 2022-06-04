n = int(input())
t_cnt = 0
f_cnt = 0
for i in range(2, n+1):
    temp = i
    while(temp % 2 == 0):
        temp /= 2
        t_cnt += 1
    while (temp % 5 == 0):
        temp /= 5
        f_cnt += 1
print(min(f_cnt, t_cnt))