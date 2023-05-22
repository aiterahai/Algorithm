from sys import stdin

vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    string = stdin.readline().rstrip()
    last = 0
    end = False

    if string == "end": break

    if not [1 for value in vowel if value in string]:
        print(f"<{string}> is not acceptable.")
        end = True
    if end: continue

    for value in string:
        if value in vowel:
            if last > 0: last += 1
            else: last = 1
        else:
            if last > 0: last = -1
            else: last -= 1
        if abs(last) == 3:
            print(f"<{string}> is not acceptable.")
            end = True
            break
    if end: continue

    board = [1]
    for idx, value in enumerate(string):
        if not idx: continue
        if string[idx - 1] == string[idx]: board.append(board[-1] + 1)
        else: board.append(1)

    for idx, value in enumerate(board):
        if value > 2:
            print(f"<{string}> is not acceptable.")
            end = True
            break
        if value == 2:
            if string[idx] == "e" or string[idx] == "o":
                continue
            else:
                print(f"<{string}> is not acceptable.")
                end = True
                break

    if end: continue
    print(f"<{string}> is acceptable.")