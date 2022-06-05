n = input()
sum = 0
if n[0] == "A": sum += 4
elif n[0] == "B": sum += 3
elif n[0] == "C": sum += 2
elif n[0] == "D": sum += 1
else:
    print(0.0)
    exit(0)
if n[1] == "+": sum += 0.3
elif n[1] == "0": sum += 0.0
elif n[1] == "-": sum += -0.3
print(sum)