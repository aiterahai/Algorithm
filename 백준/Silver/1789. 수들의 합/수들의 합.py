S = int(input())
i = 0
while True:
    i += 1
    S -= i
    if S < 0: break
print(i - 1)