n = int(input())
count = 1
sum = 0
while(n != 0):
    if (10 ** count) * 9 / 10 < n:
        if(count == 1): sum += 9
        else: sum += count * (10 ** count) * 9 / 10
        n -= (10 ** count) * 9 / 10
        count += 1
    else:
        sum += n * count
        n = 0
print(int(sum))