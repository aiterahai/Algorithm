n = int(input())
count = 0
triple_six_count = 0
while True:
    if '666' in str(count): triple_six_count += 1
    if triple_six_count == n:
        print(count)
        break
    count += 1