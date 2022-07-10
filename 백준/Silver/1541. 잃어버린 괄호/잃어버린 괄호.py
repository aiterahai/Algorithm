command = input()

result = []
buffer = ""
for i in command:
    if i == "+" or i == "-":
        result.append(int(buffer))
        result.append(i)
        buffer = ""
    else: buffer += i
result.append(int(buffer))
while True:
    try:
        t = result.index("+")
        result = result[:t-1] + [result[t-1] + result[t+1]] + result[t+2:]
    except:
        break
while True:
    try:
        t = result.index("-")
        result = result[:t-1] + [result[t-1] - result[t+1]] + result[t+2:]
    except:
        break
print(result[0])